from domain.gdk_wallet import GdkWallet

class WalletService:
    def __init__(self) -> None:
        self._wallet: GdkWallet = None
    
    """is_logged returns True in case of wallet is ready to be used"""
    def _is_logged(self) -> bool:
        if not self._wallet:
            return False
        
        return self._wallet.is_logged_in()
    
    def get_wallet(self) -> GdkWallet:
        if not self._is_logged():
            raise Exception('Wallet is ready (locked or not set up)')
        return self._wallet
    
    def generate_seed(self) -> str:
        return self.generate_seed()
    
    def create_wallet(self, mnemonic: str, password: str) -> None:
        if self._is_logged():
            raise Exception('Wallet is already logged in') 
    
        self._wallet = GdkWallet.create_new_wallet(mnemonic, password)

    def login(self, password: str) -> None:
        if self._is_logged():
            raise Exception('Wallet is already logged in')
        
        self._wallet = GdkWallet.login_with_pin(password)
    
    def change_password(self, password: str, newPassword: str) -> None:
        pass
    