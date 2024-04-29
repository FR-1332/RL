from typing import List

from pydantic import BaseModel


class State(BaseModel):
    state: List[float]
    accumulated_reward: float


class Transition(BaseModel):
    from_state: State
    actions: List[int]
    rewards: List[float]
    to_state: State


class History(BaseModel):
    transitions: List[Transition]
