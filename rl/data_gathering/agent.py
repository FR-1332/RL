from gym import Space
from gym.spaces.space import T_cov


class Agent:
    action_space: Space

    def __init__(self, action_space: Space):
        super().__init__()
        self.action_space = action_space

    def select_action(self, observation):
        pass


class Uniform(Agent):
    def __init__(self, environment):
        super().__init__(environment.get_action_space())

    def select_action(self, observation) -> T_cov:
        return self.action_space.sample()
