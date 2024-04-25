from concurrent.futures import ThreadPoolExecutor

from rl.data_gathering.history_gatherer import get_histories_in_parallel
from rl.data_gathering.history_store import HistoryStore

executor = ThreadPoolExecutor()
history_store = HistoryStore()

if __name__ == "__main__":
    with executor as executor:
        history_store.save_multiple(histories=get_histories_in_parallel(executor, amount=1000))

    print("finished")
