# This cell imports %%execwritefile command (executes cell and writes it into file).
#from custommagics import CustomMagics
#get_ipython().register_magics(CustomMagics)

import numpy as np
from collections import defaultdict

import matplotlib.pyplot as plt
import sys


assert sys.version_info[:3] >= (3, 6, 0), "Make sure you have Python 3.6 installed!"

from gridworld import GridworldEnv
env = GridworldEnv()

def policy_eval_v(policy, env, discount_factor=1.0, theta=0.00001):
    """
    Evaluate a policy given an environment and a full description of the environment's dynamics.

    Args:
        policy: [S, A] shaped matrix representing the policy.
        env: OpenAI env. env.P represents the transition probabilities of the environment.
            env.P[s][a] is a list of transition tuples (prob, next_state, reward, done).
            env.nS is a number of states in the environment.
            env.nA is a number of actions in the environment.
        theta: We stop evaluation once our value function change is less than theta for all states.

        discount_factor: Gamma discount factor.

    Returns:
        Vector of length env.nS representing the value function.
    """
    # Start with a all 0 value function
    V = np.zeros(env.nS)
    # YOUR CODE HERE
    while True:
        delta = 0
        for state in range(env.nS):
            v = V[state]  # Current value of the state
            sum_policy_state_action = 0
            
            for action in range(env.nA):
                sum_state_action = 0
                for prob, next_state, reward, done in env.P[state][action]:
                    sum_state_action += prob * (reward + discount_factor * V[next_state] * (not done))
                sum_policy_state_action += policy[state][action] * sum_state_action
            
            V[state] = sum_policy_state_action  # Update the value function
            delta = max(delta, abs(v - V[state]))  # Update the change in value function
        
        # Check for convergence
        if delta < theta:
            break
        
    return V

def plot_gridworld_value(V):
    plt.figure()
    c = plt.pcolormesh(V, cmap='gray')
    plt.colorbar(c)
    plt.gca().invert_yaxis()  # In the array, first row = 0 is on top
    plt.show()

def policy_iter_v(env, policy_eval_v=policy_eval_v, discount_factor=1.0):
    """
    Policy Iteration Algorithm. Iteratively evaluates and improves a policy
    until an optimal policy is found.

    Args:
        env: The OpenAI envrionment.
        policy_eval_v: Policy Evaluation function that takes 3 arguments:
            policy, env, discount_factor.
        discount_factor: gamma discount factor.

    Returns:
        A tuple (policy, V).
        policy is the optimal policy, a matrix of shape [S, A] where each state s
        contains a valid probability distribution over actions.
        V is the value function for the optimal policy.

    """
    # Start with a random policy
    policy = np.ones([env.nS, env.nA]) / env.nA
    # YOUR CODE HERE
    while True:

        V = policy_eval_v(policy, env, discount_factor=discount_factor)

        policy_stable = True  

        for state in range(env.nS):
            old_policy = policy[state].copy()

            action_values = np.zeros(env.nA)
            for action in range(env.nA):
                for prob, next_state, reward, done in env.P[state][action]:
                    action_values[action] += prob * (reward + discount_factor * V[next_state])

            # make actions a probability distirbution (softwax lol)
            exp_action_values = np.exp(action_values - np.max(action_values))
            policy[state] = exp_action_values / np.sum(exp_action_values)

            if not np.allclose(old_policy, policy[state]):
                policy_stable = False

        if policy_stable:
            break

    return policy, V

# Let's see what it does
policy, v = policy_iter_v(env, policy_eval_v)
print("Policy Probability Distribution:")
print(policy)
print("")

def print_grid_policy(policy, symbols=["^", ">", "v", "<"]):
    symbols = np.array(symbols)
    for row in policy:
        print("".join(symbols[row]))

print("Reshaped Grid Policy (0=up, 1=right, 2=down, 3=left):")
print(np.reshape(np.argmax(policy, axis=1), env.shape))
print_grid_policy(np.reshape(np.argmax(policy, axis=1), env.shape))
print("")

print("Value Function:")
print(v)
print("")

print("Reshaped Grid Value Function:")
print(v.reshape(env.shape))
print("")

plot_gridworld_value(v.reshape(env.shape))
print('done')