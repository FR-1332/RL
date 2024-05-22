import asyncio
from concurrent.futures import ProcessPoolExecutor

import httpx

import web
from agent import Agent, Uniform
from environment import Environment, OpenAIGym
from model import History


def get_one_history(agent: Agent, environment: Environment) -> History:
    while environment.is_alive:
        agent.perceive_and_memorize(environment.reward, environment.state, environment.is_alive)

        agent.select_and_memorize_action()

        environment.sample_next(agent.action)

    agent.perceive_and_memorize(environment.reward, environment.state, environment.is_alive)

    return agent.memory


def farm_and_save_loop():
    environment = OpenAIGym()
    agent = Uniform(action_space=environment.action_space)
    asyncio.run(create_requests(agent, environment))


async def create_requests(agent, environment):
    async with httpx.AsyncClient() as client:
        responses = []
        while True:
            responses.append(await send_to_web(agent, environment, client))


async def send_to_web(agent, environment, client):
    history = get_one_history(agent=agent, environment=environment)
    await web.save_one_history(history=history, client=client)


if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        loops = [pool.submit(farm_and_save_loop) for i in range(2)]
        for loop in loops:
            loop.result()
