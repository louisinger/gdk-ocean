from domain.receiver import Receiver
from domain.utxo import to_grpc_utxo
from services.transaction import TransactionService
from ocean.v1alpha import transaction_pb2, transaction_pb2_grpc

class GrpcTransactionServicer(transaction_pb2_grpc.TransactionServiceServicer):
    def __init__(self, transactionService: TransactionService):
        self._svc = transactionService
    
    def SelectUtxos(self, request: transaction_pb2.SelectUtxosRequest, context) -> transaction_pb2.SelectUtxosResponse:
        coinselection = self._svc.select_utxos(request.account_key.name, request.target_asset, request.target_amount)
        utxos = map(lambda utxo: to_grpc_utxo(utxo), coinselection.utxos)
        return transaction_pb2.SelectUtxosResponse(
            utxos=utxos,
            change=coinselection.change,
        )
    
    def EstimateFees(self, request: transaction_pb2.EstimateFeesRequest) -> transaction_pb2.EstimateFeesResponse:
        fee_amount = self._svc.estimate_fees()
        return transaction_pb2.EstimateFeesResponse(fee_amount=fee_amount)
    
    def SignTransaction(self, request: transaction_pb2.SignTransactionRequest) -> transaction_pb2.SignTransactionResponse:
        signed = self._svc.sign_transaction(request.tx_hex)
        return transaction_pb2.SignTransactionResponse(tx_hex=signed)
    
    def BroadcastTransaction(self, request: transaction_pb2.BroadcastTransactionRequest) -> transaction_pb2.BroadcastTransactionResponse:
        txid = self._svc.broadcast_transaction(request.tx_hex)
        return transaction_pb2.BroadcastTransactionResponse(txid=txid)
    
    def CreatePset(self, request: transaction_pb2.CreatePsetRequest) -> transaction_pb2.CreatePsetResponse:
        pass
    
    def UpdatePset(self, request, context):
        pass
    
    def BlindPset(self, request, context):
        pass
    
    def SignPset(self, request, context):
        pass
    
    def Mint(self, request, context):
        pass
    
    def Remint(self, request, context):
        pass
    
    def Burn(self, request, context):
        pass
    
    def Transfer(self, request: transaction_pb2.TransferRequest) -> transaction_pb2.TransferResponse:
        receivers = map(lambda receiver: Receiver(address=receiver["address"], sats=receiver["amount"], asset=receiver["asset"]), request.receivers)
        transfer_tx = self._svc.transfer(request.account_key.name, receivers)
        return transaction_pb2.TransferResponse(tx_hex=transfer_tx)
    
    def PegInAddress(self, request, context):
        pass
    
    def ClaimPegIn(self, request, context):
        pass