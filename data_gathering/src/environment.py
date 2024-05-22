from typing import Any, Callable

import gym
import numpy

from model import State, ActionSpace, Reward, Action


class Environment:
    sample_next: Callable[[Action], tuple[Reward, State]]

    action_space: ActionSpace

    reward: float = 0.
    state: State
    is_alive: bool = False


class OpenAIGym(Environment):
    _np_state: numpy.ndarray

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self._gym = gym.make("CartPole-v1")
        self._info: dict = {}
        self.action_space = self._gym.action_space
        self.is_alive = True
        self._np_state, self._info = self._gym.reset()
        self.state = self._np_state.tolist()

    def sample_next(self, action: Action):
        assert self.is_alive
        self._np_state, self.reward, is_terminated, is_truncated, self._info = self._gym.step(action=action)
        self.state = self._np_state.tolist()
        self.is_alive = not is_terminated and not is_truncated
