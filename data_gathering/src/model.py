from gym.core import ObsType, ActType
from gym.spaces.space import T_cov, Space
from pydantic import BaseModel

State = tuple[float] | ObsType
Action = T_cov
ActionSpace = Space[ActType]
Reward = float


class Rewards(BaseModel):
    accumulated: list[Reward] = []
    last: list[Reward] = []

    def perceive(self, reward: Reward):
        self.last.append(reward)
        self.accumulated.append(self.accumulated[-1] + reward if self.accumulated[-1] is not None else reward)


class History(BaseModel):
    states: list[State] = []
    actions: list[Action] = []
    is_terminal: list[bool] = []
    rewards = Rewards()
