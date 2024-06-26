from fastapi import FastAPI, Body

from model import History
from store import ListBased, HistoryStore

api = FastAPI()
history_store: HistoryStore = ListBased()


@api.post("/api/save_one_history/")
def save_one_history(json=Body(...)):
    history = History.model_validate_json(json)
    history_store.save_one(history)


@api.get("/api/get_one_history")
def get_one_history(*weights: float) -> str:
    return history_store.get_one_history(*weights).model_dump_json()
