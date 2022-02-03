from domain.gdk_wallet import GdkWallet

def wallet_guard(wallet: GdkWallet) -> None:
    if not wallet.is_logged_in():
        raise Exception('Wallet is not logged in')