import asyncio
import logging
from typing import Dict, TypedDict
from xmlrpc.client import boolean
from domain.utxo import Utxo
from typing import List
import time

LOCKTIME_SECONDS = 90

class Outpoint(TypedDict):
    txid: str
    index: int

class Locker():
    def __init__(self) -> None:
        self._locked_outpoints: Dict[int, List[Outpoint]] = {}
        
        """custom set in the locker, taking into account the lock time"""
    def _add_outpoint_to_locker(self, outpoint: Outpoint) -> None:
        free_at = int(time.time()) + LOCKTIME_SECONDS
        currently_locked = self._locked_outpoints.get(free_at)
        if not currently_locked:
            self._locked_outpoints[free_at] = [outpoint]
        else:
            currently_locked.append(outpoint)
            self._locked_outpoints[free_at] = currently_locked

        """check if the outpoint is in the locker, ideally you should first call _free_locker() before calling this method"""
    def _is_in_locker(self, outpoint: Outpoint) -> boolean:
        if not self._locked_outpoints:
            return False
        
        all_outpoints = [outpoint for outpoints in self._locked_outpoints.values() for outpoint in outpoints]
        if outpoint in all_outpoints:
            return True
        
        return False
        
        """free all the outpoints that are in the locker with time <= now"""
    def _free_locker(self):
        now = int(time.time())
        for locked_time in self._locked_outpoints.keys():
            if locked_time <= now:
                freed = self._locked_outpoints.pop(locked_time)
                for freed_outpoint in freed:
                    # todo notification!!
                    logging.debug(f"Unlocked {freed_outpoint}")
                    
                return True

        """lock an utxo for a certain amount of time, defined by LOCKTIME_SECONDS"""
    def lock(self, utxo: Utxo) -> None:
        outpoint = Outpoint(txid=utxo["txid"], index=utxo["index"])
        self._add_outpoint_to_locker(outpoint)

        """checks if the utxo is locked"""
    def is_locked(self, outpoint: Outpoint) -> bool:
        self._free_locker() # remove all free outpoints
        return self._is_in_locker(outpoint)
        