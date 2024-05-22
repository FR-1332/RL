from gym.core import ObsType, ActType
from gym.spaces.space import T_cov, Space
from pydantic import BaseModel, ConfigDict

State = tuple[float, ...] | ObsType
Action = T_cov
ActionSpace = Space[ActType]
Reward = float


class Rewards(BaseModel):
    accumulated: list[Reward] = []
    last: list[Reward] = []

    def append(self, reward: Reward):
        self.last.append(reward)
        self.accumulated.append(self.accumulated[-1] + reward if len(self.accumulated) > 0 else reward)


class History(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    actions: list[Action] = []
    rewards: Rewards = Rewards()
    states: list[State] = []
    is_alive: list[bool] = []

    def append(self, reward: Reward, state: State, is_alive: bool):
        self.rewards.append(reward)
        self.states.append(state)
        self.is_alive.append(is_alive)
