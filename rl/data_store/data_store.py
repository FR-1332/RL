from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


@dataclass
class Record:
    observation: Any
    action: int
    reward: float


class DataStore(BaseModel):
    def __init__(self, /, **data: Any):
        super().__init__(**data)
        raise NotImplementedError

    def store(self, history: tuple[Record, ...]):
        pass


class ListBased(DataStore):
    histories = []

    def store(self, history: tuple[Record, ...]):
        self.histories.append(history)
