
def sample_episode(env, policy):
    """
    A sampling routine. Given environment and a policy samples one episode and returns states, actions, rewards
    and dones from environment's step function and policy's sample_action function as lists.

    Args:
        env: OpenAI gym environment.
        policy: A policy which allows us to sample actions with its sample_action method.

    Returns:
        Tuple of lists (states, actions, rewards, dones). All lists should have same length.
        Hint: Do not include the state after the termination in the list of states.
    """
    states = []
    actions = []
    rewards = []
    dones = []

    state = env.reset()
    states.append(state)
    while True:
        action = policy.sample_action(states[-1])
        actions.append(action)

        observation, reward, done, info = env.step(actions[-1])

        rewards.append(reward)
        dones.append(done)

        if dones[-1]:
            break

        print("------------------")
        print(f"Observarion: {observation}")
        print(f"Action: {action}")
        print(f"Done: {done}")
        
        states.append(observation)
        

    # YOUR CODE HERE
    return states, actions, rewards, dones

def sample_episode(env, policy):
    """
    A sampling routine. Given environment and a policy samples one episode and returns states, actions, rewards
    and dones from environment's step function and policy's sample_action function as lists.

    Args:
        env: OpenAI gym environment.
        policy: A policy which allows us to sample actions with its sample_action method.

    Returns:
        Tuple of lists (states, actions, rewards, dones). All lists should have same length.
        Hint: Do not include the state after the termination in the list of states.
    """
    states = []
    actions = []
    rewards = []
    dones = []

    state = env.reset()
    states.append(state)
    while True:
        action = policy.sample_action(states[-1])
        actions.append(action)

        observation, reward, done, info = env.step(actions[-1])

        rewards.append(reward)
        dones.append(done)

        if dones[-1]:
            break

        print("------------------")
        print(f"Observarion: {observation}")
        print(f"Action: {action}")
        print(f"Done: {done}")
        
        states.append(observation)
        

    # YOUR CODE HERE
    return states, actions, rewards, dones

def sample_episode(env, policy):
    """
    A sampling routine. Given environment and a policy samples one episode and returns states, actions, rewards
    and dones from environment's step function and policy's sample_action function as lists.

    Args:
        env: OpenAI gym environment.
        policy: A policy which allows us to sample actions with its sample_action method.

    Returns:
        Tuple of lists (states, actions, rewards, dones). All lists should have same length.
        Hint: Do not include the state after the termination in the list of states.
    """
    states = []
    actions = []
    rewards = []
    dones = []

    state = env.reset()
    states.append(state)
    while True:
        action = policy.sample_action(states[-1])
        actions.append(action)

        observation, reward, done, info = env.step(actions[-1])

        rewards.append(reward)
        dones.append(done)

        if dones[-1]:
            break

        print("------------------")
        print(f"Observarion: {observation}")
        print(f"Action: {action}")
        print(f"Done: {done}")
        
        states.append(observation)
        

    # YOUR CODE HERE
    return states, actions, rewards, dones

def sample_episode(env, policy):
    """
    A sampling routine. Given environment and a policy samples one episode and returns states, actions, rewards
    and dones from environment's step function and policy's sample_action function as lists.

    Args:
        env: OpenAI gym environment.
        policy: A policy which allows us to sample actions with its sample_action method.

    Returns:
        Tuple of lists (states, actions, rewards, dones). All lists should have same length.
        Hint: Do not include the state after the termination in the list of states.
    """
    states = []
    actions = []
    rewards = []
    dones = []

    state = env.reset()
    states.append(state)
    while True:
        action = policy.sample_action(states[-1])
        actions.append(action)

        observation, reward, done, info = env.step(actions[-1])

        rewards.append(reward)
        dones.append(done)

        if dones[-1]:
            break

        print("------------------")
        print(f"Observarion: {observation}")
        print(f"Action: {action}")
        print(f"Done: {done}")
        
        states.append(observation)
        

    # YOUR CODE HERE
    return states, actions, rewards, dones
