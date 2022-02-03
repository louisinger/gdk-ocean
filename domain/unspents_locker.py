import asyncio
from typing import TypedDict
from domain.utxo import Utxo
from typing import List

LOCKTIME_SECONDS = 60

class Outpoint(TypedDict):
    txid: str
    index: int

class UtxosLocker():
    def __init__(self) -> None:
        self.locked_outpoints: List[Outpoint] = []
        
    async def _unlock_after(self, outpoint: Outpoint) -> None:
        asyncio.sleep(LOCKTIME_SECONDS)
        self.locked_outpoints.remove(outpoint)
        
    def lock(self, utxo: Utxo) -> None:
        outpoint = Outpoint(txid=utxo.txid, index=utxo.index)
        self.locked_outpoints.append(outpoint)
        asyncio.create_task(self._unlock_after(outpoint))
    
    def is_locked(self, outpoint: Outpoint) -> bool:
        return outpoint in self.locked_outpoints