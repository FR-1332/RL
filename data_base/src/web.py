from fastapi import FastAPI

from model import History
from store import HistoryStore

api = FastAPI()
history_store = HistoryStore()


@api.post("/")
def save_one_history(history: History) -> None:
    history_store.save_one_history(history=history)


@api.get("/")
def get_one_history(*weights: float) -> History:
    return history_store.get_one_history(*weights)
