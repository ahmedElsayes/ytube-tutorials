
import numpy as np
import random
import gym

env = gym.make("Taxi-v3").env
env.render()

action_size = env.action_space.n
print("Action size ", action_size)
state_size = env.observation_space.n
print("State size ", state_size)

qtable = np.zeros((state_size, action_size))
print(qtable)

# Defining Hyperparameters**************************************************************************
total_episodes = 50000        # Total episodes
total_test_episodes = 100     # Total test episodes
max_steps = 99                # Max steps per episode
learning_rate = 0.1          # Learning rate
gamma = 0.6                 # Discounting rate
# Exploration parameters
epsilon = 0.2                 # Exploration rate
max_epsilon = 0.2             # Exploration probability at start
min_epsilon = 0.01            # Minimum exploration probability
decay_rate = 0.01             # Exponential decay rate for exploration prob

# Traing Agent*****************************************************************************


# Testing agent ******************************************************************
env.reset()
rewards = []
for episode in range(total_test_episodes):
    state = env.reset()
    step = 0
    done = False
    total_rewards = 0
    #print("*****************")
    #print("EPISODE ", episode)

    for step in range(max_steps):
        # UNCOMMENT IT IF YOU WANT TO SEE OUR AGENT PLAYING
        # env.render()
        # Take the action (index) that have the maximum expected future reward given that state
        action = np.argmax(qtable[state, :])

        new_state, reward, done, info = env.step(action)

        total_rewards += reward

        if done:
            rewards.append(total_rewards)
            #print ("Score", total_rewards)
            break
        state = new_state
env.close()
print("Score over time: " + str(sum(rewards)/total_test_episodes))

print("Total reward: ")
print(sum(rewards))
print("Total actions: ")
print(total_test_episodes)