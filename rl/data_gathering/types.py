from typing import Any, List

from pydantic.dataclasses import dataclass


@dataclass
class State:
    state: Any
    accumulated_reward: float


@dataclass
class Transition:
    from_state: State
    actions: List[int]
    rewards: List[float]
    to_state: State


History = List[Transition]
