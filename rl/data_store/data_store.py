"""
The data store.
"""

from dataclasses import dataclass
from typing import Any, List

from pydantic import BaseModel


@dataclass
class Record(BaseModel):
    """
    Basic form of the RL data.
    """
    observation: Any
    action: int
    reward: float


class DataStore(BaseModel):
    """
    Interface
    """

    def store(self, history: tuple[Record, ...]):
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

    def store(self, history: tuple[Record, ...]):
        self.histories.append(history)
