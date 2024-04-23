"""
The data gatherer.
"""
import concurrent.futures

from pydantic import BaseModel

from rl.data_gathering.agent import Agent
from rl.data_gathering.data_store import Record
from rl.data_gathering.environment import Environment


class DataGatherer(BaseModel):
    """
    Implementation.
    """
    environment: Environment
    agent: Agent

    def __init__(self, environment_class: Environment.__class__, agent_class: Agent.__class__):
        super().__init__()
        self.environment = environment_class()
        self.agent = agent_class(self.environment)

    def get_history(self):
        history = []
        observation = self.environment.reset()
        while self.environment.is_alive:
            action = self.agent.select_action(observation)
            resulting_observation, reward = self.environment.do_action(action)
            reaction = Record(observation=observation, action=action, reward=reward)
            history.append(reaction)
            observation = resulting_observation
        return tuple(history)

    def get_histories_in_parallel(self, amount: int):
        with concurrent.futures.ThreadPoolExecutor as executor:
            return executor.map(fn=self.get_history, *range(amount))
