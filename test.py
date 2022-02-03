import asyncio
from domain import GdkWallet
import greenaddress as gdk
from handlers.grpc_notifications import GrpcNotificationsServicer
from services.notifications import NotificationsService

async def wait_notif(q: asyncio.Queue):
    while True:
        print("waiting for notification...")
        n = await q.get()
        print("--> NOTIFICATION", n)
        q.task_done()

async def main():
    gdk.init({})
    print("Hello World!")
    wallet = GdkWallet.create_new_wallet(
        "sleep high awkward police test stick tiger warfare emerge illness bright leader",
        "12456",
        "testnet-liquid"
    )
    
    # print(wallet.get_account('AMP Account').get_all_utxos(False))
    print(wallet.get_account('AMP Account').get_new_address()["address"])
    
    notifSvc = NotificationsService(wallet)
    notifSvc.add_txs_check_account("AMP Account")
    notifSvc.add_utxos_check_account("AMP Account")
    
    grpc = await GrpcNotificationsServicer.create(notifSvc)

    
asyncio.run(main())