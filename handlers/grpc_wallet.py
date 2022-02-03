from ocean.v1alpha import wallet_pb2, wallet_pb2_grpc
from services.wallet import WalletService

class GrpcWalletServicer(wallet_pb2_grpc.WalletServiceServicer):
    def __init__(self, walletService: WalletService):
        self._svc = walletService
    
    def GenSeed(self):
        return wallet_pb2.GenSeedResponse(signing_mnemonic=self._svc.generate_seed())
    
    def CreateWallet(self, request: wallet_pb2.CreateWalletRequest):
        self._svc.create_wallet(request.mnemonic, request.password)
        return wallet_pb2.CreateWalletResponse()
    
    def Unlock(self, request: wallet_pb2.UnlockRequest):
        self._svc.login(request.password)
        return wallet_pb2.UnlockReply()
    
    def ChangePassword(self, request: wallet_pb2.ChangePasswordRequest):
        self._svc.change_password(request.current_password, request.newPassword)
        return wallet_pb2.ChangePasswordResponse()
    
    def RestoreWallet(self, request: wallet_pb2.RestoreWalletRequest):
        self._svc.login(request.password)
        return wallet_pb2.RestoreWalletResponse()

    def Status(self):
        if self._svc.is_logged_in():
            return wallet_pb2.StatusResponse(status=wallet_pb2.Status.OPEN)

        return wallet_pb2.StatusResponse(status=wallet_pb2.Status.CLOSED)
            
    def GetInfo(self, request: wallet_pb2.GetInfoRequest):
        return wallet_pb2.GetInfoResponse() # TODO