import asyncio
import logging
from typing import Dict, Set, TypedDict, List
from domain.gdk_wallet import GdkWallet
from domain.notification import BaseNotification, TxConfirmedNotification, UtxoSpentNotification, UtxoUnspecifiedNotification
from domain.utxo import Utxo
from services.wallet import WalletService

def _get_utxos_by_account(wallet: GdkWallet) -> Dict[str, Dict[str, List[Utxo]]]:
    utxos_by_account: Dict[str, Dict[str, List[Utxo]]] = {}
    
    for name, account in wallet.accounts.items():
        utxos = account.get_all_utxos(False)
        utxos_by_account[name] = utxos
    
    return utxos_by_account    

# def _get_transactions_by_account(wallet: GdkWallet, account: str) -> Dict[str, List[]]:

def _diff_utxos_list(current: Dict[str, List[Utxo]], new: Dict[str, List[Utxo]], account: str) -> List[BaseNotification]:
    if not current:
        current = {}
    if not new:
        new = {}
    
    notifs: List[BaseNotification] = []
    
    current_list: List[Utxo] = []
    new_list: List[Utxo] = []
    
    for utxos in current.values():
        current_list.extend(utxos)
    
    for utxos in new.values():
        new_list.extend(utxos)
        
    for utxo in new_list:
        if utxo not in current_list:
            notifs.append(UtxoUnspecifiedNotification(utxo, account))
    
    for utxo in current_list:
        if utxo not in new_list:
            notifs.append(UtxoSpentNotification(utxo, account))
    
    return notifs

class BlockNotification(TypedDict):
    block_hash: str
    block_height: int

class NotificationsService():
    def __init__(self, wallet_svc: WalletService):
        self._wallet_svc = wallet_svc
        self._started = False
        
        self.queue = asyncio.Queue()
        
        # the accounts to compute diff from
        self._utxos_check_accounts: Set[str] = set()

        # init the state
        try:
            wallet = self._wallet_svc.get_wallet() 
            self._utxos_by_account = _get_utxos_by_account(wallet)
        except:
            self._utxos_by_account = {}    
    
    async def _put_in_queue(self, notification: BaseNotification, queue: asyncio.Queue) -> None:
        logging.debug("new notification {} put in queue".format(notification.type))
        await queue.put(notification)
    
    async def _put_utxos_notifications(self, queue: asyncio.Queue) -> None:
        wallet = self._wallet_svc.get_wallet()
        new_utxos_by_account = _get_utxos_by_account(wallet)
        
        for account_name in self._utxos_check_accounts:
            utxos_notifications = _diff_utxos_list(self._utxos_by_account.get(account_name), new_utxos_by_account.get(account_name), account_name)
            for notification in utxos_notifications:
                await self._put_in_queue(notification, queue)
        # update the cache with the new state
        self._utxos_by_account = new_utxos_by_account
    
    async def _put_confirmed_txs_notifications(self, height: int, block_hash: str, queue: asyncio.Queue) -> None:
        wallet = self._wallet_svc.get_wallet()
        all_accounts_names = list(wallet.accounts.keys())
        for account_name in all_accounts_names:
            try:
                account = wallet.get_account(account_name)
                txs_for_height = account.get_transactions(height)
                tx_confirmed_notifications = [TxConfirmedNotification(tx['txhash'], block_hash, height) for tx in txs_for_height] 
                for notif in tx_confirmed_notifications:
                    await self._put_in_queue(notif, queue)
            except:
                continue
    
    
    async def _wait_for_wallet(self) -> GdkWallet:
        wallet = None
        while wallet is None:
            try:
                wallet = self._wallet_svc.get_wallet()
            except:
                await asyncio.sleep(2)
        return wallet

    async def _handle_gdk_notifications(self, queue: asyncio.Queue) -> None:
        wallet = await self._wait_for_wallet()
        gdk_notifications = wallet.session.notifications

        async def next_notification():
            while True:
                try:
                    return gdk_notifications.get(block=False)
                except:
                    await asyncio.sleep(0.5)

        while self._started:
            notification = await next_notification()
            event = notification['event']
            
            if event == 'block':
                logging.debug(f"new block: {notification['block']['block_height']} {notification['block']['block_hash']}")
                block = BlockNotification(notification['block'])
                # compute notifications from new state each time we get a block
                await self._put_utxos_notifications(queue=queue)
                await self._put_confirmed_txs_notifications(block['block_height'], block['block_hash'], queue=queue)
                await queue.join() # wait a bit to let notifications consumers get the queue

            await asyncio.sleep(1)
        
    def _check_not_started(self):
        if self._started:
            raise Exception('NotificationsService started')
        
    def add_utxos_check_account(self, account_name: str) -> None:
        self._utxos_check_accounts.add(account_name)
    
    def remove_utxos_check_account(self, account_name: str) -> None:
        self._utxos_check_accounts.remove(account_name)
    
    async def start(self) -> None:
        self._check_not_started()
        self._started = True
        await self._handle_gdk_notifications(self.queue)
    
    def stop(self):
        self._started = False
        