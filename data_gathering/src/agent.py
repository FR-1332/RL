from gym import Space
from gym.spaces.space import T_cov
from pydantic import BaseModel, ConfigDict


class Uniform(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    action_space: Space

    def get_uniform_sample_action(self, state) -> T_cov:
        return self.action_space.sample()


class Agent(Uniform):

    def select_action(self, state):
        return self.get_uniform_sample_action(state=state)
