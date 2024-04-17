"""
The data store.
"""

from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


@dataclass
class Record:
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

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        raise NotImplementedError

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
    histories = []

    def store(self, history: tuple[Record, ...]):
        self.histories.append(history)
