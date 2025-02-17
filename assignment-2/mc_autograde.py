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

def mc_prediction(policy, env, num_episodes, discount_factor=1.0, sampling_function=sample_episode):
    """
    Monte Carlo prediction algorithm. Calculates the value function
    for a given policy using sampling.

    Args:
        policy: A policy which allows us to sample actions with its sample_action method.
        env: OpenAI gym environment.
        num_episodes: Number of episodes to sample.
        discount_factor: Gamma discount factor.
        sampling_function: Function that generates data from one episode.

    Returns:
        A dictionary that maps from state -> value.
        The state is a tuple and the value is a float.
    """

    # Keeps track of current V and count of returns for each state
    # to calculate an update.
    V = defaultdict(float)
    returns_count = defaultdict(float)

    # YOUR CODE HERE
    for i in tqdm(range(num_episodes)):
        episode = sampling_function(env=env, policy=policy)
        G = 0
        for step in range(len(episode[0]) - 1, -1, -1):
            state = episode[0][step]
            G = discount_factor * G + episode[2][step]
            returns_count[state] += 1 # why not appending G instead of 1?
            V[state] = G * (1/returns_count[state]) + V[state] * ((returns_count[state] - 1) / returns_count[state])

    return V

class RandomBlackjackPolicy(object):
    """
    A random BlackJack policy.
    """
    def get_probs(self, states, actions):
        """
        This method takes a list of states and a list of actions and returns a numpy array that contains
        a probability of perfoming action in given state for every corresponding state action pair.

        Args:
            states: a list of states.
            actions: a list of actions.

        Returns:
            Numpy array filled with probabilities (same length as states and actions)
        """

        # YOUR CODE HERE
        probs = np.random.rand(len(states))
        probs = probs/np.sum(probs)

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
        action = np.random.choice([0, 1], p=self.get_probs([state, state], [0,1]))
        #action = np.argmax(self.get_probs([state, state], [0, 1]))
        return action

# we need to implement ORDINARY importance sampling! I think it's book equation 5.5

def mc_importance_sampling(behavior_policy, target_policy, env, num_episodes, discount_factor=1.0,
                           sampling_function=sample_episode):
    """
    Monte Carlo prediction algorithm. Calculates the value function
    for a given target policy using behavior policy and ordinary importance sampling.

    Args:
        behavior_policy: A policy used to collect the data.
        target_policy: A policy which value function we want to estimate.
        env: OpenAI gym environment.
        num_episodes: Number of episodes to sample.
        discount_factor: Gamma discount factor.
        sampling_function: Function that generates data from one episode.

    Returns:
        A dictionary that maps from state -> value.
        The state is a tuple and the value is a float.
    """

    # Keeps track of current V and count of returns for each state
    # to calculate an update.
    V = defaultdict(float)
    returns_count = defaultdict(float)

    # YOUR CODE HERE
    # you got this hehe ;)

    for i in tqdm(range(num_episodes)):
        episode = sampling_function(env=env, policy=behavior_policy)
        G = 0
        W = 1
        for step in range(len(episode[0]) - 1, -1, -1):
            state = episode[0][step]
            G = discount_factor * G + episode[2][step]   

            # Compute importance sampling ratio
            action = behavior_policy.sample_action(state)
            b_a_given_s = behavior_policy.get_probs([state],[action])  # Probability of action under target policy
            pi_a_given_s = target_policy.get_probs([state],[action])  # Probability of action under behavior policy
            if b_a_given_s == 0:  # Avoid division by zero
                break
            W *= pi_a_given_s / b_a_given_s

            # Update value function using ordinary importance sampling formula
            returns_count[state] += 1
            V[state] += (W * G - V[state]) / returns_count[state]  # Incremental update

    return V

    """
    THIS IS TRASH LOL. 
    for i in tqdm(range(num_episodes)):
        episode = sample_episode(env=env, policy=behavior_policy)
        G = 0
        for step in range(len(episode[0]) - 1, -1, -1):
            state = episode[0][step]
            G = discount_factor * G + episode[2][step]    
            returns_count[state] += 1
            timestamps = get_timestamps(episode, state)    
            cum_sum = 0
            for timestamp in timestamps:
                cum_sum += get_p(episode, behavior_policy, target_policy, timestamp, step)
            V[state] = 

    return V

    THIS IS FROM PREVIOUS EXCERCISE BC I THOUGHT IT WOULD BE SIMILAR BUT IDK
    for i in tqdm(range(num_episodes)):
        episode = sampling_function(env=env, policy=policy)
        G = 0
        for step in range(len(episode[0]) - 1, -1, -1):
            state = episode[0][step]
            G = discount_factor * G + episode[2][step]
            returns_count[state] += 1
            V[state] = G * (1/returns_count[state]) + V[state] * ((returns_count[state] - 1) / returns_count[state])

    return V
    """
