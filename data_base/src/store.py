import random
from fractions import Fraction
from typing import List, Iterable, Callable

from model import History


class HistoryStore:
    save_one: Callable[[History], None]
    save_multiple: Callable[[Iterable[History]], None]
    get_one_history: Callable[[tuple[float | Fraction]], History]


class ListBased(HistoryStore):
    def __init__(self):
        self.histories: List[History] = []

    def save_one_history(self, history: History) -> None:
        self.histories.append(history)

    def save_multiple(self, histories: Iterable[History]) -> None:
        self.histories.extend(histories)

    def get_one_history(self, *weights: float | Fraction) -> History:
        return random.choices(population=self.histories, weights=weights, k=1)
