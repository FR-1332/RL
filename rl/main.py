import concurrent.futures
from itertools import count

from rl.data_gathering.agent import Uniform
from rl.data_gathering.data_gatherer import DataGatherer
from rl.data_gathering.environment import Gym
from rl.data_store.data_store import ListBased

if __name__ == '__main__':
    store = ListBased()
    gatherer = DataGatherer(Gym, Uniform)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for history in executor.map(gatherer.gather_one_history, count()):
            store.store(history)
