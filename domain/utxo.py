from typing import TypedDict, List
from ocean.v1alpha import types_pb2

class Utxo(TypedDict):
    txid: str
    index: int
    asset: str
    value: int
    script: str
    is_confirmed: bool
    is_locked: bool

def to_grpc_utxo(utxo: Utxo) -> types_pb2.Utxo:
    return types_pb2.Utxo(
        txid=utxo['txid'],
        index=utxo['index'],
        asset=utxo['asset'],
        value=utxo['value'],
        script=utxo['script'],
        is_confirmed=utxo['is_confirmed'],
        is_locked=utxo['is_locked']
    )
    
class CoinSelectionResult(TypedDict):
    asset: str
    total: int
    change: int
    utxos: List[Utxo]