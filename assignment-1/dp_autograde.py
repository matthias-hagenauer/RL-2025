import numpy as np
from collections import defaultdict

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
    delta = np.inf
    while delta > theta:
        for state in range(env.nS):
            v = V[state].copy()
            sum_policy_state_action = 0
            for action in range(env.nA):
                sum_state_action = 0
                for prob, next_state, reward, done in env.P[state][action]:
                    sum_state_action += * prob * (reward + discount_factor * V[next_state])
                sum_policy_state_action += policy[state][action] * sum_state_action
            V[state] = sum_policy_state_action
            delta = max([delta, np.sum(abs(v - V[state]))])
        
    return np.array(V)

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
    delta = np.inf
    while delta > theta:
        for state in range(env.nS):
            v = V[state].copy()
            sum_policy_state_action = 0
            for action in range(env.nA):
                sum_state_action = 0
                for prob, next_state, reward, done in env.P[state][action]:
                    sum_state_action += prob * (reward + discount_factor * V[next_state])
                sum_policy_state_action += policy[state][action] * sum_state_action
            V[state] = sum_policy_state_action
            delta = max([delta, np.sum(abs(v - V[state]))])
        
    return np.array(V)

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
    delta = theta * 2
    while delta > theta:
        for state in range(env.nS):
            v = V[state].copy()
            sum_policy_state_action = 0
            for action in range(env.nA):
                sum_state_action = 0
                for prob, next_state, reward, done in env.P[state][action]:
                    sum_state_action += prob * (reward + discount_factor * V[next_state])
                sum_policy_state_action += policy[state][action] * sum_state_action
            V[state] = sum_policy_state_action
            delta = max([delta, np.sum(abs(v - V[state]))])
        
    return np.array(V)

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
    delta = theta * 1.0000001
    while delta > theta:
        for state in range(env.nS):
            v = V[state].copy()
            sum_policy_state_action = 0
            for action in range(env.nA):
                sum_state_action = 0
                for prob, next_state, reward, done in env.P[state][action]:
                    sum_state_action += prob * (reward + discount_factor * V[next_state])
                sum_policy_state_action += policy[state][action] * sum_state_action
            V[state] = sum_policy_state_action
            delta = max([delta, np.sum(abs(v - V[state]))])
        
    return np.array(V)

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
            v = V[state]
            sum_policy_state_action = 0
            for action in range(env.nA):
                sum_state_action = 0
                for prob, next_state, reward, done in env.P[state][action]:
                    sum_state_action += prob * (reward + discount_factor * V[next_state])
                sum_policy_state_action += policy[state][action] * sum_state_action
            V[state] = sum_policy_state_action
            delta = max(delta, abs(v - V[state]))

        if delta < theta:
            break
        
    return np.array(V)
