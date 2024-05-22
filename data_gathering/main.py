import asyncio
from concurrent.futures import ProcessPoolExecutor

import httpx

import web
from agent import Agent, Uniform
from environment import Environment, OpenAIGym
from model import History


def get_one_history(agent: Agent, environment: Environment) -> History:
    state = environment.sample_initial()
    agent.perceive_state(state=state)

    while not environment.is_terminal:
        action = agent.select_action()

        reward, state = environment.sample_next(action)
        agent.perceive_reward(reward=reward)
        agent.perceive_state(state=state)

    agent.memory.is_terminal.append(True)

    return agent.memory


def farm_and_save_loop():
    environment = OpenAIGym()
    agent = Uniform(action_space=environment.get_action_space())
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
