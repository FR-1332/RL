from concurrent.futures import Executor
from math import sqrt
from threading import Lock
from typing import List

from rl.data_gathering.agent import Agent
from rl.data_gathering.environment import Environment
from rl.data_gathering.types import State, Transition, History


def get_histories_in_parallel(executor: Executor, amount: int) -> List[History]:
    rounded_sqrt = round(sqrt(amount))
    gatherers = [HistoryGatherer() for i in range(rounded_sqrt)]
    futures = [executor.submit(lambda: gatherer.get_histories_sequentially(amount=rounded_sqrt)) for gatherer in
               gatherers]
    histories = []
    for future in futures:
        histories.extend(future.result())
    return histories


lock = Lock()


class HistoryGatherer:
    def __init__(self):
        self.environment = Environment()
        self.agent = Agent(action_space=self.environment.environment.action_space)

    def get_one_history(self) -> History:
        with lock:
            history: History = []
            from_state = State(state=self.environment.sample_initial(), accumulated_reward=0)
            while not self.environment.is_terminal:
                action = self.agent.select_action(from_state.state)
                state, reward = self.environment.sample_next(action=action)
                to_state = State(state=state, accumulated_reward=from_state.accumulated_reward + reward)
                transition = Transition(from_state=from_state, actions=[action], rewards=[reward],
                                        to_state=to_state)
                history.append(transition)
                from_state = to_state
            return history

    def get_histories_sequentially(self, amount: int):
        return [self.get_one_history() for i in range(amount)]
