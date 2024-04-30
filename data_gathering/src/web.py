from httpx import AsyncClient

from model import History


async def save_one_history(history: History, client: AsyncClient):
    json = history.model_dump_json()
    response = await client.post(url='http://localhost:8000/api/save_one_history/', json=json)
    return response
