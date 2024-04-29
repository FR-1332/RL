import asyncio
from concurrent.futures import ProcessPoolExecutor

import web
from agent import Agent
from environment import Environment
from model import History, State, Transition


def get_one_history(agent: Agent, environment: Environment) -> History:
    history: History = History(transitions=[])
    from_state = State(state=environment.sample_initial(), accumulated_reward=0)
    while not environment.is_terminal:
        action = agent.select_action(from_state.state)
        state, reward = environment.sample_next(action=action)
        to_state = State(state=state, accumulated_reward=from_state.accumulated_reward + reward)
        transition = Transition(from_state=from_state, actions=[action], rewards=[reward],
                                to_state=to_state)
        history.transitions.append(transition)
        from_state = to_state
    return history


def farm_and_save_loop():
    environment = Environment()
    agent = Agent(action_space=environment.environment.action_space)
    responses = []
    while True:
        responses.append(farm_and_save(agent, environment))


def farm_and_save(agent, environment):
    history = get_one_history(agent=agent, environment=environment)
    return asyncio.run(web.save_one_history(history=history))


if __name__ == "__main__":
    with ProcessPoolExecutor() as pool:
        loops = [pool.submit(farm_and_save_loop) for i in range(2)]
        for loop in loops:
            loop.result()
