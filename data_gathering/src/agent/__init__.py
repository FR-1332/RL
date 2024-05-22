from typing import Any, Callable

from agent.algo import TreeSampler
from model import Action, History, ActionSpace, State, Reward


class Algo:
    select_action: Callable[[], Action]


class Agent:
    _select_action: Callable[[], Action]
    memory = History()

    def perceive_state(self, state: State):
        self.memory.states.append(state)
        self.memory.is_terminal.append(False)

    def select_action(self):
        action = self._select_action()
        self.memory.actions.append(action)
        return action

    def perceive_reward(self, reward: Reward):
        self.memory.rewards.perceive(reward=reward)


class Uniform(Agent):

    def __init__(self, action_space: ActionSpace, **data: Any):
        super().__init__(**data)
        self._action_space = action_space

    def _select_action(self) -> Action:
        return self._action_space


class Kekw(Agent):

    def _select_action(self) -> Action:
        tree_sampler = TreeSampler(self.memory.states[-1])
        tree_sampler.sample()
        return Action
