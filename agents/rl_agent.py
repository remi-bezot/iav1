# import gym

# class RLAgent:
#     def __init__(self, env):
#         self.env = env
#         self.model = self.build_model()

#     def build_model(self):
#         # Initialisation de l'agent avec un modèle simple
#         pass

#     def train(self):
#         # Entraînement de l'agent
#         pass

import gym
import tensorflow as tf
from tensorflow.keras import layers

class RLAgent:
    def __init__(self, env_name):
        self.env = gym.make(env_name)
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            layers.Dense(24, activation='relu', input_shape=(self.env.observation_space.shape[0],)),
            layers.Dense(24, activation='relu'),
            layers.Dense(self.env.action_space.n, activation='linear')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, episodes=1000):
        for e in range(episodes):
            state = self.env.reset()
            done = False
            while not done:
                action = self.env.action_space.sample()  # Action aléatoire, peut être optimisé
                next_state, reward, done, _ = self.env.step(action)
                self.model.fit(state, reward, epochs=1, verbose=0)
                state = next_state
