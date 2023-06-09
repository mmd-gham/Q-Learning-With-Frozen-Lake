import numpy as np
import gym
import random
import time
from math import e

################################ set environment and variables ##############################

env = gym.make('FrozenLake-v1', desc=None ,map_name="4x4", is_slippery=False, render_mode='ansi')
action_size = env.action_space.n  # 4 action
state_size = env.observation_space.n #16 state
qtable = np.zeros((state_size, action_size))

print("Init Qtable:\n ")
print(qtable)
total_episodes = 200           # Total episodes
learning_rate = 0.5            # Learning rate
max_steps = 20                 # Max steps per episode
gamma = 0.9                    # Discounting rate
epsilon = 1          #initialize the exploration probability to 1
epsilon_decay = 0.001    #exploartion decreasing decay for exponential decreasing


rewards_per_episode = list()


######################################### Game is on ##########################
print("training...")
for episode in range(total_episodes):
    state = env.reset()[0]         # Reset the environment and init state is given
    step = 0
    done = False
    total_episode_reward = 0       # sum the rewards that the agent gets from the environment
    # print("EPISODE: ",episode)
    for step in range(max_steps):
        
        ## Generate a random number between 0 and 1
        rnd = np.random.random()
        
        if rnd < epsilon:
            action = env.action_space.sample()           # random action, sample returns the format of action left,right,up,own            
        else:
            action = np.argmax(qtable[state,:])
            
       
        new_state, reward, done,truncated, info = env.step(action)
        #Somehow, the environment does not give negative rewards for game over, so hack it:
        if done and reward == 0:
            reward = -5
        if new_state == state:
            reward = -1
        # print("NEW STATE:",new_state,"REWARD:",reward)
        qtable[state, action] = qtable[state, action] + learning_rate * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])
        # qtable[state, action]=reward + gamma * np.max(qtable[new_state, :]) # max=best action for newstate * gama  #storing tha data of step in qtable
        # print("QTABLE AT",state,qtable[state])
        state = new_state
        total_episode_reward = total_episode_reward + reward
        if done: 
            print("GAME OVER.\n\n")
            break
    # print("new QTABLE")
    # print(qtable)
    
    
    # Update epsilon
    epsilon = max(epsilon - epsilon_decay, 0)
    rewards_per_episode.append(total_episode_reward)


env.reset()
env.close()
print("result is going on")
print(qtable)


################################### evaluation ###############################
env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False,render_mode='human')
state = env.reset()[0]
step = 0
done = False
print("****************************************************")
for step in range(6):
        env.render()
        action = np.argmax(qtable[state,:])  # argmax returns the index from the qtable , max is the best action
        new_state, reward, done,truncated, info = env.step(action)
        if done:
            break
        state = new_state
   
        
print(rewards_per_episode) 
# time.sleep(2)
env.reset()
env.close()
















