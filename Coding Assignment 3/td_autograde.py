import numpy as np
from collections import defaultdict
from tqdm import tqdm as _tqdm

def tqdm(*args, **kwargs):
    return _tqdm(*args, **kwargs, mininterval=1)  # Safety, do not overflow buffer

class EpsilonGreedyPolicy(object):
    """
    A simple epsilon greedy policy.
    """
    def __init__(self, Q, epsilon):
        self.Q = Q
        self.epsilon = epsilon
    
    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.  

        Args:
            state: current state

        Returns:
            An action (int).
        """
        
        # YOUR CODE HERE
        #raise NotImplementedError
        if np.random.rand() < self.epsilon:
            return np.random.randint(len(self.Q[state]))
        else:
            return np.argmax(self.Q[state])
        
        return action

def sarsa(env, policy, Q, num_episodes, discount_factor=1.0, alpha=0.5):
    """
    SARSA algorithm: On-policy TD control. Finds the optimal epsilon-greedy policy.
    
    Args:
        env: OpenAI environment.
        policy: A policy which allows us to sample actions with its sample_action method.
        Q: Q value function, numpy array Q[s,a] -> state-action value.
        num_episodes: Number of episodes to run for.
        discount_factor: Gamma discount factor.
        alpha: TD learning rate.
        
    Returns:
        A tuple (Q, stats).
        Q is a numpy array Q[s,a] -> state-action value.
        stats is a list of tuples giving the episode lengths and returns.
    """
    
    # Keeps track of useful statistics
    stats = []
    
    for i_episode in tqdm(range(num_episodes)):
        i = 0 
        R = 0 
        
        # YOUR CODE HERE
        #raise NotImplementedError
        S = env.reset()
        A = policy.sample_action(S)
        while True:
            S1, reward, done, _ = env.step(A)
            R += reward
            A1 = policy.sample_action(S1) if not done else None
            if not done:
                Q[S,A] += alpha*(reward+discount_factor*Q[S1,A1]-Q[S,A])
            else:
                Q[S,A] += alpha*(reward-Q[S,A])
            S = S1
            A = A1
            i+=1
            if done:
                break

        stats.append((i, R))
    episode_lengths, episode_returns = zip(*stats)
    return Q, (episode_lengths, episode_returns)
