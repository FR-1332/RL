import httpx
from pydantic import validate_call

from model import History


@validate_call
async def save_one_history(history: History):
    async with httpx.AsyncClient() as client:
        json = history.model_dump_json()
        response = await client.post(url='http://localhost:8000/api/save_one_history/', json=json)
        return response
