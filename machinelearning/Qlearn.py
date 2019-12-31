
import numpy as np
import gym
import random

env = gym.make("Taxi-v3")

env.reset()  # reset environment to a new, random state
env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))
