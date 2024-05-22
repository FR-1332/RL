from typing import Callable

from model import State


class TreeSampler:
    sampled_states: list[State] = []

    def __init__(self, root_state: State):
        self.root_state = root_state

    sample: Callable[[], State]
    
