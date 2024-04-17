from typing import Any

import gym
from gym import Env, Space
from pydantic import BaseModel


class Environment(BaseModel):
    env: Env
    action_space: Space

    is_alive: bool

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        raise NotImplementedError

    def do_action(self, action: int):
        pass

    def get_env(self):
        pass

    def reset(self):
        pass


class Gym(Environment):
    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self.env = gym.make("CartPole-v1")

    def do_action(self, action: int):
        observation, reward, terminated, truncated, info = self.env.step(action)
        self.is_alive = ((not terminated) & (not truncated))
        return observation, reward

    def get_env(self):
        return self.env

    def get_action_space(self):
        return self.env.action_space

    def reset(self):
        initial_state, info = self.env.reset()
        return initial_state
