import os
import pytest
import wallycore as wally

from domain import FilePinDataRepository, make_session, Locker, GdkAPI, InMemoryPinDataRepository
from services import TransactionService, WalletService, AccountService

TEST_PASSWORD = 'testdonotuse'

testnet_test_mnemonic = 'TESTNET_TEST_MNEMONIC'
if os.environ.get(testnet_test_mnemonic) is not None:
    TEST_MNEMONIC = os.environ[testnet_test_mnemonic]
else:
    from dotenv import load_dotenv
    load_dotenv()
    TEST_MNEMONIC = os.environ[testnet_test_mnemonic]

@pytest.mark.asyncio
async def test_send_pset():
    accountName = 'mainAccountTest'
    session = make_session('testnet-liquid')
    locker = await Locker.create()
    transactionSvc = TransactionService(session, locker)
    accountSvc = AccountService(session, locker)
    walletSvc = WalletService(session, InMemoryPinDataRepository())
    walletSvc.create_wallet(TEST_MNEMONIC, TEST_PASSWORD)

    addrs = accountSvc.derive_address(accountName, 2)
    coinSelection = transactionSvc.select_utxos(accountName, '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 100000)
    FEE = 500
    
    gdkAPI = GdkAPI(session)
    
    lbtc = '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49'
    outputs = [
        { 'address': addrs[0]['address'], 'amount': coinSelection.amount - FEE, 'asset': lbtc, 'blinder_index': 0 },
    ]
    
    if coinSelection.change > 0:
        outputs += [{ 'address': addrs[1]['address'], 'amount': coinSelection.change, 'asset': lbtc, 'blinder_index': 0 }]
    
    outputs += [{ 'address': None, 'amount': FEE, 'asset': lbtc, 'blinder_index': None }]
    
    psetb64 = transactionSvc.create_pset([u.to_pset_input_args() for u in coinSelection.utxos], outputs)
    blinded = transactionSvc.blind_pset(psetb64)
    signed = transactionSvc.sign_pset(blinded)
    assert signed is not None

    pset = wally.psbt_from_base64(signed)
    wally.psbt_finalize(pset)
    tx = wally.psbt_extract(pset)
    assert tx is not None

@pytest.mark.asyncio
async def test_send_amp_confidential_pset():
    accountName = 'mainAccountTest'
    ampAccountName = 'ampAccountTest'
    session = make_session('testnet-liquid')
    walletSvc = WalletService(session, FilePinDataRepository('pin_data.json'))
    walletSvc.create_wallet(TEST_MNEMONIC, TEST_PASSWORD)
    # walletSvc.login_with_pin(TEST_PASSWORD)
    lockerSvc = await Locker.create()
    accountSvc = AccountService(session, lockerSvc)
    transactionSvc = TransactionService(session, lockerSvc)

    FEE = 500
    fees_selection = transactionSvc.select_utxos(accountName, '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', FEE)
    amp_selection = transactionSvc.select_utxos(ampAccountName, 'bea126b86ac7f7b6fc4709d1bb1a8482514a68d35633a5580d50b18504d5c322', 1)
    receiveAddr = 'vjTvPHdcJFZrYL9LmFpPootd1tmWqzugF9MXwhet6cdeCKEK6WJrb2mPEQGw7WNpikAoTq9ui22GU2pS' 

    outputs = [
        {'address': receiveAddr, 'amount': 1, 'asset': 'bea126b86ac7f7b6fc4709d1bb1a8482514a68d35633a5580d50b18504d5c322', 'blinder_index': 0},
    ]
    
    if fees_selection.change > 0:
        changeAddr = accountSvc.derive_address(accountName, 1)[0]
        outputs += [{ 'address': changeAddr['address'], 'amount': fees_selection.change, 'asset': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 'blinder_index': 0 }]
    
    outputs += [{'address': None, 'amount': FEE, 'asset': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 'blinder_index': None}]

    b64 = transactionSvc.create_pset(
        [u.to_pset_input_args() for u in fees_selection.utxos] + [u.to_pset_input_args() for u in amp_selection.utxos], 
        outputs
    )
    
    blinded = transactionSvc.blind_pset(b64)
    signed = transactionSvc.sign_pset(blinded)    
    assert signed is not None

    pset = wally.psbt_from_base64(signed)
    wally.psbt_finalize(pset)
    tx = wally.psbt_extract(pset)
    assert tx is not None
    
@pytest.mark.asyncio
async def test_send_fee_nonlast_amp_confidential_pset():
    accountName = 'mainAccountTest'
    ampAccountName = 'ampAccountTest'
    session = make_session('testnet-liquid')
    walletSvc = WalletService(session, FilePinDataRepository('pin_data.json'))
    walletSvc.create_wallet(TEST_MNEMONIC, TEST_PASSWORD)
    # walletSvc.login_with_pin(TEST_PASSWORD)
    lockerSvc = await Locker.create()
    accountSvc = AccountService(session, lockerSvc)
    transactionSvc = TransactionService(session, lockerSvc)

    FEE = 500
    fees_selection = transactionSvc.select_utxos(accountName, '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', FEE)
    amp_selection = transactionSvc.select_utxos(ampAccountName, 'bea126b86ac7f7b6fc4709d1bb1a8482514a68d35633a5580d50b18504d5c322', 1)
    receiveAddr = 'vjTvPHdcJFZrYL9LmFpPootd1tmWqzugF9MXwhet6cdeCKEK6WJrb2mPEQGw7WNpikAoTq9ui22GU2pS' 

    outputs = [
        {'address': receiveAddr, 'amount': 1, 'asset': 'bea126b86ac7f7b6fc4709d1bb1a8482514a68d35633a5580d50b18504d5c322', 'blinder_index': 0},
        {'address': None, 'amount': FEE, 'asset': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 'blinder_index': None}
    ]
    
    if fees_selection.change > 0:
        changeAddr = accountSvc.derive_address(accountName, 1)[0]
        outputs += [{ 'address': changeAddr['address'], 'amount': fees_selection.change, 'asset': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 'blinder_index': 0 }]
    
    b64 = transactionSvc.create_pset(
        [u.to_pset_input_args() for u in fees_selection.utxos] + [u.to_pset_input_args() for u in amp_selection.utxos], 
        outputs
    )
    
    blinded = transactionSvc.blind_pset(b64)
    signed = transactionSvc.sign_pset(blinded)    
    assert signed is not None

    pset = wally.psbt_from_base64(signed)
    wally.psbt_finalize(pset)
    tx = wally.psbt_extract(pset)
    assert tx is not None

@pytest.mark.asyncio
async def buggish_mnemonic():
    mnemonic = "begin trouble invite bus reform wave crouch floor bring detect record bag"
    session = make_session('testnet-liquid')
    walletSvc = WalletService(session, FilePinDataRepository('pin_data.json'))
    walletSvc.create_wallet(mnemonic, TEST_PASSWORD)
    # walletSvc.login_with_pin(TEST_PASSWORD)
    lockerSvc = await Locker.create()
    accountSvc = AccountService(session, lockerSvc)
    transactionSvc = TransactionService(session, lockerSvc)
    # gdkAPI = GdkAPI(session)
    # accountNameMultisig = 'Securities'
    utxo0 = accountSvc.get_utxo('1f78b56be4ecb6591b4c6069e629f39470c7569d3737e7d8223cf76a77dc3015', 0)
    utxo1 = accountSvc.get_utxo('82436b9e07f0f9d909d73faade015bdcd4374961cb0e80b9a23f76b8ae444fa3', 0)


    FEE = 500
    receiveAddr = 'vjU5inAPDKufZSfr7b2y7JAmrNSdjZA2WdbAY8DySrgoQ8cKA4R6D4hDR5crxdamchiakXMoENAYyDss' 

    outputs = [
        {'address': receiveAddr, 'amount': 1, 'asset': 'bea126b86ac7f7b6fc4709d1bb1a8482514a68d35633a5580d50b18504d5c322', 'blinder_index': 0},
        {'address': None, 'amount': FEE, 'asset': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 'blinder_index': None},
        {'address': 'vjTvPHdcJFZrYL9LmFpPootd1tmWqzugF9MXwhet6cdeCKEK6WJrb2mPEQGw7WNpikAoTq9ui22GU2pS', 'amount': 100000000-FEE, 'asset': '144c654344aa716d6f3abcc1ca90e5641e4e2a7f633bc09fe3baf64585819a49', 'blinder_index': 0}
    ]
    
    b64 = transactionSvc.create_pset(
        [u.to_pset_input_args() for u in [utxo0, utxo1]], 
        outputs
    )
    
    blinded = transactionSvc.blind_pset(b64)
    print(blinded)
    signed = transactionSvc.sign_pset(blinded)    
    assert signed is not None

    pset = wally.psbt_from_base64(signed)
    wally.psbt_finalize(pset)
    tx = wally.psbt_extract(pset)
    print(tx)
    # assert tx is not None