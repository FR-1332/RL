"""
The data store.
"""
import random
from fractions import Fraction
from typing import List, Iterable

from rl.data_gathering.types import History


class ListBased:
    def __init__(self):
        self.histories: List[History] = []

    def save(self, history: History) -> None:
        self.histories.append(history)

    def save_multiple(self, histories: Iterable[History]) -> None:
        self.histories.extend(histories)

    def get_one_history(self, *weights: float | Fraction) -> History:
        return random.choices(population=self.histories, weights=weights, k=1)


class HistoryStore(ListBased):
    pass
