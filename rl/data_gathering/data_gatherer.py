"""
The data gatherer.
"""

from rl.data_gathering.agent import Agent
from rl.data_gathering.environment import Environment
from rl.data_store.data_store import Record


class DataGatherer:
    """
    Implementation.
    """
    environment: Environment
    agent: Agent

    def __init__(self, environment_class, agent_class):
        super().__init__()
        self.environment = environment_class()
        self.agent = agent_class(self.environment)

    def gather_one_history(self):
        history = []
        observation = self.environment.reset()
        while self.environment.is_alive:
            action = self.agent.select_action(observation)
            resulting_observation, reward = self.environment.do_action(action)
            reaction = Record(observation, action, reward)
            history.append(reaction)
            observation = resulting_observation
        return tuple(history)
