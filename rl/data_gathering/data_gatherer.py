from typing import Any

from pydantic import BaseModel

from agent import Agent, Uniform
from environment import Environment, Gym
from ..data_store.data_store import DataStore, Record


class DataGatherer(BaseModel):
    environment: Environment
    agent: Agent
    data_store: DataStore

    def __init__(self, /, **data: Any):
        super().__init__(**data)
        self.environment = Gym()
        self.agent = Uniform(self.environment.action_space)

    def gather_one_history(self):
        history = []
        observation = self.environment.reset()
        while self.environment.is_alive:
            action = self.agent.select_action(observation)
            resulting_observation, reward = self.environment.do_action(action)
            reaction = Record(observation, action, reward)
            history.append(reaction)
            observation = resulting_observation
        self.data_store.store(tuple(history))

    def gather(self):
        while True:
            self.gather_one_history()
