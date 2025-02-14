import numpy as np
from collections import defaultdict
from tqdm import tqdm as _tqdm

def tqdm(*args, **kwargs):
    return _tqdm(*args, **kwargs, mininterval=1)  # Safety, do not overflow buffer

class SimpleBlackjackPolicy(object):
    """
    A simple BlackJack policy that sticks with less than 20 points and hits otherwise.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains a probability
        of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """
        # YOUR CODE HERE
        probs = np.zeros((len(states, len(actions))))
        for state in range(len(states)):
            for action in range(len(actions)):
                probs[state][action] = 1 if ((states[state][0] > 19) and (actions[action] == 0)) or ((states[state][0] < 20) and (actions[action] == 1)) else 0
        
        return np.array(probs)

    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            state: current state

        Returns:
            An action (int).
        """
        # YOUR CODE HERE
        action = np.argmax(self.get_probs([state], [1, 0]))
        return action

class SimpleBlackjackPolicy(object):
    """
    A simple BlackJack policy that sticks with less than 20 points and hits otherwise.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains a probability
        of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """
        # YOUR CODE HERE
        probs = np.zeros((len(states, len(actions))))
        for state in range(len(states)):
            for action in range(len(actions)):
                probs[state][action] = 1 if ((states[state][0] > 19) and (actions[action] == 0)) or ((states[state][0] < 20) and (actions[action] == 1)) else 0
        
        return np.array(probs)

    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            state: current state

        Returns:
            An action (int).
        """
        # YOUR CODE HERE
        action = np.argmax(self.get_probs([state], [0, 1]))
        return action

class SimpleBlackjackPolicy(object):
    """
    A simple BlackJack policy that sticks with less than 20 points and hits otherwise.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains a probability
        of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """
        # YOUR CODE HERE
        probs = np.zeros((len(states), len(actions)))
        for state in range(len(states)):
            for action in range(len(actions)):
                probs[state][action] = 1 if ((states[state][0] > 19) and (actions[action] == 0)) or ((states[state][0] < 20) and (actions[action] == 1)) else 0
        
        return np.array(probs)

    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            state: current state

        Returns:
            An action (int).
        """
        # YOUR CODE HERE
        action = np.argmax(self.get_probs([state], [0, 1]))
        return action

class SimpleBlackjackPolicy(object):
    """
    A simple BlackJack policy that sticks with less than 20 points and hits otherwise.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains a probability
        of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """
        # YOUR CODE HERE
        #probs = np.zeros((len(states), len(actions)))
        #for state in range(len(states)):
        #    for action in range(len(actions)):
        #        probs[state][action] = 1 if ((states[state][0] > 19) and (actions[action] == 0)) or ((states[state][0] < 20) and (actions[action] == 1)) else 0
        
        probs = np.zeros(len(states))
        for i in range(len(states))
            probs[i] = 1 if ((states[i][0] > 19) and (actions[i] == 0)) or ((states[i][0] < 20) and (actions[i] == 1)) else 0

        return np.array(probs)

    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            state: current state

        Returns:
            An action (int).
        """
        # YOUR CODE HERE
        action = np.argmax(self.get_probs([state], [0, 1]))
        return action

class SimpleBlackjackPolicy(object):
    """
    A simple BlackJack policy that sticks with less than 20 points and hits otherwise.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains a probability
        of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """
        # YOUR CODE HERE
        #probs = np.zeros((len(states), len(actions)))
        #for state in range(len(states)):
        #    for action in range(len(actions)):
        #        probs[state][action] = 1 if ((states[state][0] > 19) and (actions[action] == 0)) or ((states[state][0] < 20) and (actions[action] == 1)) else 0
        
        probs = np.zeros(len(states))
        for i in range(len(states)):
            probs[i] = 1 if ((states[i][0] > 19) and (actions[i] == 0)) or ((states[i][0] < 20) and (actions[i] == 1)) else 0

        return np.array(probs)

    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            state: current state

        Returns:
            An action (int).
        """
        # YOUR CODE HERE
        action = np.argmax(self.get_probs([state], [0, 1]))
        return action

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
    states = states.append(state)
    while True:
        action = policy.sample_action(states[-1])
        actions = actions.append(action)
        observation, reward, done, info = env.step(actions[-1])
        rewards = rewards.append(reward)
        dones = dones.append(done)
        if dones[-1]:
            break
        states = states.append(observation)
        

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
        actions.append(action, inplace = True)
        observation, reward, done, info = env.step(actions[-1])
        rewards.append(reward)
        dones.append(done)
        if dones[-1]:
            break
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
        print(observation)
        if dones[-1]:
            break
        states.append(observation)
        

    # YOUR CODE HERE
    return states, actions, rewards, dones

class SimpleBlackjackPolicy(object):
    """
    A simple BlackJack policy that sticks with less than 20 points and hits otherwise.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains a probability
        of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """
        # YOUR CODE HERE
        #probs = np.zeros((len(states), len(actions)))
        #for state in range(len(states)):
        #    for action in range(len(actions)):
        #        probs[state][action] = 1 if ((states[state][0] > 19) and (actions[action] == 0)) or ((states[state][0] < 20) and (actions[action] == 1)) else 0
        
        probs = np.zeros(len(states))
        for i in range(len(states)):
            probs[i] = 1 if ((states[i][0] > 19) and (actions[i] == 0)) or ((states[i][0] < 20) and (actions[i] == 1)) else 0

        return np.array(probs)

    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            state: current state

        Returns:
            An action (int).
        """
        # YOUR CODE HERE
        action = np.argmax(self.get_probs([state, state], [0, 1]))
        return action

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
        print(info)

        if dones[-1]:
            break
        
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
            print(observation)
            break
        
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
        
        states.append(observation)
        

    # YOUR CODE HERE
    return states, actions, rewards, dones
