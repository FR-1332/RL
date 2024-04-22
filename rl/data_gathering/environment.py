import gym
from gym import Env


class Environment:
    env: Env

    is_alive: bool

    def do_action(self, action: int):
        pass

    def get_env(self):
        pass

    def get_action_space(self):
        pass

    def reset(self):
        pass


class Gym(Environment):
    def __init__(self):
        super().__init__()
        self.env = gym.make("CartPole-v1")

    def do_action(self, action: int):
        observation, reward, terminated, truncated, _info = self.env.step(action)
        self.is_alive = (not terminated) & (not truncated)
        return observation, reward

    def get_env(self):
        return self.env

    def get_action_space(self):
        return self.env.action_space

    def reset(self):
        initial_state, _info = self.env.reset()
        self.is_alive = True
        return initial_state
