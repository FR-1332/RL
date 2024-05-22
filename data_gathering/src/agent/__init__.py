from typing import Any, Callable

from agent.algo import TreeSampler
from model import Action, History, ActionSpace, Reward, State


class Agent:
    action: Action
    select_action: Callable[[], None]
    memory = History()

    def select_and_memorize_action(self):
        self.select_action()
        self.memory.actions.append(self.action)

    def perceive_and_memorize(self, reward: Reward, state: State, is_alive: bool):
        self.memory.append(reward, state, is_alive)


class Uniform(Agent):

    def __init__(self, action_space: ActionSpace, **data: Any):
        super().__init__(**data)
        self._action_space = action_space

    def select_action(self):
        self.action = self._action_space.sample()


class Kekw(Agent):

    def select_action(self) -> Action:
        tree_sampler = TreeSampler(self.memory.states[-1])
        tree_sampler.sample()
        return Action
