"""
The data store.
"""

from typing import List

from pydantic import BaseModel

from rl.data_gathering.types import Record


class DataStore(BaseModel):
    """
    Interface
    """

    def save(self, history: tuple[Record, ...]):
        """
        Stores the
        :param history:
        :return:
        """


class ListBased(DataStore):
    """
    Stores in a variable with Python List.
    """
    histories: List = []

    def save(self, history: tuple[Record, ...]):
        self.histories.append(history)
        
    def save_multiple(self, histories: List[tuple[Record, ...]]):
        self.histories.extend(__iterable=histories)
