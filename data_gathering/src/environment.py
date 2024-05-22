from typing import Any, Callable

import gym

from model import State, ActionSpace, Reward, Action


class Environment:
    sample_initial: Callable[[], State]
    sample_next: Callable[[Action], (Reward, State)]
    get_action_space: Callable[[], ActionSpace]

    is_terminal: bool


class OpenAIGym(Environment):

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self._gym = gym.make("CartPole-v1")
        self._info: dict = {}

        self.is_terminal = False

    def sample_initial(self) -> State:
        state, self._info = self._gym.reset()
        self.is_terminal = False
        return state

    def sample_next(self, action) -> (Reward, State):
        assert not self.is_terminal
        state, reward, is_terminated, is_truncated, self._info = self._gym.step(action=action)
        self.is_terminal = is_terminated or is_truncated
        return reward, state

    def get_action_space(self) -> ActionSpace:
        return self._gym.action_space
