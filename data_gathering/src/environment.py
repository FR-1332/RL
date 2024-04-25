import gym
from gym.core import ObsType
from pydantic import ConfigDict


class OpenAIGym:
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(self):
        self.environment = gym.make("CartPole-v1")
        self.is_terminal = False
        self.info: dict = {}

    def sample_initial(self) -> ObsType:
        state, self.info = self.environment.reset()
        self.is_terminal = False
        return state

    def sample_next(self, action) -> [ObsType, float]:
        assert not self.is_terminal
        state, reward, is_terminated, is_truncated, self.info = self.environment.step(action=action)
        self.is_terminal = is_terminated or is_truncated
        return state, reward


class Environment(OpenAIGym):
    pass
