from ocean.v1alpha import notification_pb2, types_pb2
from domain.utxo import Utxo
from enum import Enum

class NotificationType(Enum):
    UTXO_SPENT = 0
    UTXO_LOCKED = 1
    UTXO_UNLOCKED = 2
    UTXO_UNSPECIFIED = 3
    
    TX_BROADCASTED = 4
    TX_CONFIRMED = 5
    TX_UNCONFIRMED = 6
    TX_UNSPECIFIED = 7


class BaseNotification():
    def __init__(self) -> None:
        self.type: NotificationType = None

class UtxoNotification(BaseNotification):
    def __init__(self, n_type: NotificationType, data: Utxo, account_name: str):
        self.type = n_type
        self.data = data
        self.account_name = account_name
        
    def _type_to_tx_event_type(self) -> types_pb2.UtxoEventType:
        if self.type is NotificationType.UTXO_SPENT:
            return types_pb2.UTXO_EVENT_TYPE_SPENT
        elif self.type is NotificationType.UTXO_LOCKED:
            return types_pb2.UTXO_EVENT_TYPE_LOCKED
        elif self.type is NotificationType.UTXO_UNSPECIFIED:
            return types_pb2.UTXO_EVENT_TYPE_UNSPECIFIED
        elif self.type is NotificationType.UTXO_UNLOCKED:
            return types_pb2.UTXO_EVENT_TYPE_UNLOCKED
        else:
            raise Exception(f"Unknown utxo event type: {self.type}")
    
    def to_proto(self) :
        return None
            
    
class UtxoSpentNotification(UtxoNotification):
    def __init__(self, utxo: Utxo):
        super().__init__('utxo_spent', utxo)
        
class UtxoUnspecifiedNotification(UtxoNotification):
    def __init__(self, utxo: Utxo):
        super().__init__('utxo_unspecified', utxo)
    

class TxNotification(BaseNotification):
    def __init__(self, n_type: NotificationType, txid: str, block_height: int, block_hash: str):
        self.type = n_type
        self.data = {
            "txid": txid,
            "block_height": block_height,
            "block_hash": block_hash,
        }
    
    def _type_to_tx_event_type(self) -> types_pb2.TxEventType:
        if self.type is NotificationType.TX_CONFIRMED:
            return types_pb2.TX_EVENT_TYPE_CONFIRMED
        elif self.type is NotificationType.TX_UNCONFIRMED:
            return types_pb2.TX_EVENT_TYPE_UNCONFIRMED
        elif self.type is NotificationType.TX_UNSPECIFIED:
            return types_pb2.TX_EVENT_TYPE_UNSPECIFIED
        elif self.type is NotificationType.TX_BROADCASTED:
            return types_pb2.TX_EVENT_TYPE_BROADCASTED
        else:
            raise Exception(f"Unknown tx event type: {self.type}")
    
    def to_proto(self) -> notification_pb2.TransactionNotificationsResponse:
        return notification_pb2.TransactionNotificationsResponse(
            txid=self.data["txid"],
            event_type=self._type_to_tx_event_type(),
            block_height=self.data["block_height"],
            block_hash=self.data["block_hash"],
        )
        
class TxConfirmedNotification(TxNotification):
    def __init__(self, txid: str, block_hash: str, block_height: int):
        super().__init__('tx_confirmed', txid, block_height, block_hash)
    
class TxUnconfirmedNotification(TxNotification):
    def __init__(self, txid: str, block_height: int, block_hash: str):
        super().__init__('tx_unconfirmed', txid, block_height, block_hash)

class TxUnspecifiedNotification(TxNotification):
    def __init__(self, txid: str, block_height: int, block_hash: str):
        super().__init__('tx_unspecified', txid, block_height, block_hash)
