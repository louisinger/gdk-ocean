from services.account import AccountService
from ocean.v1alpha import account_pb2, account_pb2_grpc

class GrpcAccountServicer(account_pb2_grpc.AccountServiceServicer):
    def __init__(self, accountService: AccountService) -> None:
        self._svc = accountService
    
    def CreateAccount(self, request: account_pb2.CreateAccountRequest) -> account_pb2.CreateAccountResponse:
        self._svc.create_account(request.account_key.name)
        return account_pb2.CreateAccountResponse()
    
    def SetAccountTemplate(self, request, context):
        pass
    
    def DeriveAddress(self, request: account_pb2.DeriveAddressRequest, context):
        addresses = self._svc.derive_address(request.account_key.name, request.num_of_addresses)
        return account_pb2.DeriveAddressResponse(addresses=map(lambda address: address['address'], addresses))
    
    def ListAddresses(self, request: account_pb2.ListAddressesRequest):
        addresses = self._svc.list_addresses(request.account_key.name)
        return account_pb2.ListAddressesResponse(
            addresses=map(lambda address: address['address'], addresses)
        )
    
    def Balance(self, request: account_pb2.BalanceRequest, context) -> account_pb2.BalanceResponse:
        balance = self._svc.balance(request.account_key.name)
        return account_pb2.BalanceResponse(balance=balance)

    def ListUtxos(self, request: account_pb2.ListUtxosRequest, context):
        return super().ListUtxos(request, context)