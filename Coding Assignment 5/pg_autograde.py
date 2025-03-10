import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from tqdm import tqdm as _tqdm

def tqdm(*args, **kwargs):
    return _tqdm(*args, **kwargs, mininterval=1)  # Safety, do not overflow buffer

class NNPolicy(nn.Module):
    
    def __init__(self, num_hidden=128):
        nn.Module.__init__(self)
        self.l1 = nn.Linear(4, num_hidden)
        self.l2 = nn.Linear(num_hidden, 2)

    def forward(self, x):
        """
        Performs a forward pass through the network.
        
        Args:
            x: input tensor (first dimension is a batch dimension)
            
        Return:
            Probabilities of performing all actions in given input states x. Shape: batch_size x action_space_size
        """
        
        # YOUR CODE HERE
        relu = nn.ReLU()
        output_1 = self.l1(x)
        output_2 = relu(output_1)
        output_3 = self.l2(output_2)
        output_4 = F.softmax(output_3, dim = -1)

        return output_4

    def get_probs(self, state, actions):
        """
        This function takes a tensor of states and a tensor of actions and returns a tensor that contains 
        a probability of perfoming corresponding action in all states (one for every state action pair). 

        Args:
            state: a tensor of states. Shape: batch_size x obs_dim
            actions: a tensor of actions. Shape: batch_size x 1

        Returns:
            A torch tensor filled with probabilities. Shape: batch_size x 1.
        """
        
        # YOUR CODE HERE
        all_probs = self.forward(state)
        action_probs = all_probs.gather(1, actions.long())
        
        return action_probs
    
    def sample_action(self, state):
        """
        This method takes a state as input and returns an action sampled from this policy.  

        Args:
            state: state as a tensor. Shape: 1 x obs_dim or obs_dim

        Returns:
            An action (int).
        """
        
        # YOUR CODE HERE
        all_probs = self.forward(state)
        distribution = torch.distributions.Categorical(probs=all_probs)
        action = distribution.sample().item()
        
        return action
        
        

def sample_episode(env, policy):
    """
    A sampling routine. Given environment and a policy samples one episode and returns states, actions, rewards
    and dones from environment's step function as tensors.

    Args:
        env: OpenAI gym environment.
        policy: A policy which allows us to sample actions with its sample_action method.

    Returns:
        Tuple of tensors (states, actions, rewards, dones). All tensors should have same first dimension and 
        should have dim=2. This means that vectors of length N (states, rewards, actions) should be Nx1.
        Hint: Do not include the state after termination in states.
    """
    states = []
    actions = []
    rewards = []
    dones = []
    
    # YOUR CODE HERE
    state = env.reset()
    
    done = False
    while not done:
        states.append(state)
        
        action = policy.sample_action(torch.FloatTensor(state))
        actions.append(action)
        
        next_state, reward, done, _ = env.step(action)
        
        rewards.append(reward)
        dones.append(done)
        
        state = next_state
    
    states = torch.tensor(states, dtype=torch.float32).unsqueeze(-1)
    actions = torch.tensor(actions, dtype=torch.float32).unsqueeze(-1)
    rewards = torch.tensor(rewards, dtype=torch.float32).unsqueeze(-1)
    dones = torch.tensor(dones, dtype=torch.float32).unsqueeze(-1)


    return states, actions, rewards, dones

def compute_reinforce_loss(policy, episode, discount_factor):
    """
    Computes reinforce loss for given episode.

    Args:
        policy: A policy which allows us to get probabilities of actions in states with its get_probs method.

    Returns:
        loss: reinforce loss
    """
    # Compute the reinforce loss
    # Make sure that your function runs in LINEAR TIME
    # Note that the rewards/returns should be maximized 
    # while the loss should be minimized so you need a - somewhere
    
    # YOUR CODE HERE
    #raise NotImplementedError
    states, actions, rewards, _ = episode
    states = states.view(-1, 4)
    G = torch.zeros_like(rewards)
    running_return = 0
    for t in reversed(range(len(rewards))):
        running_return = rewards[t] + discount_factor * running_return
        G[t] = running_return
    log_probs = torch.log(policy.get_probs(states, actions.long().view(-1, 1)))
    loss = -torch.sum(log_probs * G)
    
    return loss

def run_episodes_policy_gradient(policy, env, num_episodes, discount_factor, learn_rate, 
                                 sampling_function=sample_episode):
    optimizer = optim.Adam(policy.parameters(), learn_rate)
    
    episode_durations = []
    for i in range(num_episodes):
        
        # YOUR CODE HERE
        #raise NotImplementedError
        episode = sampling_function(env, policy)
        loss = compute_reinforce_loss(policy, episode, discount_factor)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
                           
        if i % 10 == 0:
            print("{2} Episode {0} finished after {1} steps"
                  .format(i, len(episode[0]), '\033[92m' if len(episode[0]) >= 195 else '\033[99m'))
        episode_durations.append(len(episode[0]))
        
    return episode_durations


