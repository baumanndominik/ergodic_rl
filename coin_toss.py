import gym
import numpy as np
from gym import spaces


class Coin_toss(gym.Env):
	"""Custom Environment that follows gym interface."""

	metadata = {"render.modes": ["human"]}

	def __init__(self, ergodic=True, trans=None):
		super().__init__()
		self.action_space = spaces.Box(low=1e-10, high=0.99999, shape=(1,), dtype=np.float32)
		self.observation_space = spaces.Box(low=0, high=1e10,
											shape=(1,), dtype=np.float32)
		self.cum_reward = 100
		self.episode_steps = 0
		self.max_episode_steps = 100
		self.ergodic = ergodic
		if trans is not None:
			self.trans = trans 
		else:
			self.trans = np.log

	def _get_info(self):
		return {"wealth": self.cum_reward}

	def step(self, action):
		if self.cum_reward < 1e-10:
			self.cum_reward = 1e-10
		self.episode_steps += 1
		cum_reward_old = self.cum_reward
		bet = action*self.cum_reward
		if np.random.randint(2) == 1:
			reward = 0.6*bet
		else:
			reward = 1.5*bet
		self.cum_reward = self.cum_reward - bet + reward
		reward_out = reward
		observation = self.cum_reward
		done = False 
		info = self._get_info()  
		if self.episode_steps > self.max_episode_steps:
			done = True
		if self.ergodic:
			return self.trans(observation), (self.trans(self.cum_reward) - self.trans(cum_reward_old)).item(), done, info
		else:
			return observation, reward_out.item(), done, info

	def reset(self):
		self.cum_reward = 100
		observation = self.cum_reward
		self.episode_steps = 0
		return np.array([observation])  

	def render(self, mode="human"):
		return

	def close(self):
		self.cum_reward = 100
		self.episode_steps = 0
		super.close()
