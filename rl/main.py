from rl.data_gathering import agent, environment, data_gatherer, data_store

if __name__ == "__main__":
    store = data_store.ListBased()
    gatherer = data_gatherer.DataGatherer(environment_class=environment.Gym, agent_class=agent.Uniform)
    while True:
        history = gatherer.get_histories_in_parallel(amount=128)
        store.save(history=history)
