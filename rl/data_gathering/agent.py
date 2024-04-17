from typing import Any

from gym import Space
from gym.spaces.space import T_cov
from pydantic import BaseModel


class Agent(BaseModel):
    action_space: Space

    def __init__(self, action_space: Space, /, **data: Any):
        super().__init__(**data)
        self.action_space = action_space
        raise NotImplementedError

    def select_action(self, observation):
        pass


class Uniform(Agent):
    def __init__(self, action_space: Space, /, **data: Any):
        super().__init__(action_space, **data)

    def select_action(self, observation) -> T_cov:
        return self.action_space.sample()
