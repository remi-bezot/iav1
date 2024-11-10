# import numpy as np
# import random
# from collections import deque
# import tensorflow as tf
# from tensorflow.keras import layers, Model

# class DQNAgent:
#     def __init__(self, state_size, action_size):
#         self.state_size = state_size
#         self.action_size = action_size
#         self.memory = deque(maxlen=2000)
#         self.model = self._build_model()
#         self.gamma = 0.95
#         self.epsilon = 1.0
#         self.epsilon_min = 0.01
#         self.epsilon_decay = 0.995

#     def _build_model(self):
#         model = tf.keras.Sequential()
#         model.add(layers.Dense(24, input_dim=self.state_size, activation='relu'))
#         model.add(layers.Dense(24, activation='relu'))
#         model.add(layers.Dense(self.action_size, activation='linear'))
#         model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam())
#         return model

#     def remember(self, state, action, reward, next_state, done):
#         self.memory.append((state, action, reward, next_state, done))

#     def act(self, state):
#         if np.random.rand() <= self.epsilon:
#             return random.choice(range(self.action_size))
#         act_values = self.model.predict(state)
#         return np.argmax(act_values[0])

#     def replay(self, batch_size):
#         if len(self.memory) < batch_size:
#             return
#         minibatch = random.sample(self.memory, batch_size)
#         for state, action, reward, next_state, done in minibatch:
#             target = reward
#             if not done:
#                 target += self.gamma * np.max(self.model.predict(next_state)[0])
#             target_f = self.model.predict(state)
#             target_f[0][action] = target
#             self.model.fit(state, target_f, epochs=1, verbose=0)
#         if self.epsilon > self.epsilon_min:
#             self.epsilon *= self.epsilon_decay


import numpy as np
import random
from collections import deque
import tensorflow as tf
from tensorflow.keras import layers

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.model = self._build_model()
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995

    def _build_model(self):
        model = tf.keras.Sequential()
        model.add(layers.Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(layers.Dense(24, activation='relu'))
        model.add(layers.Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam())
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(range(self.action_size))
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target += self.gamma * np.max(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def check_convergence(self):
        # Méthode pour vérifier si l'amélioration du modèle est suffisante
        # À implémenter selon des critères spécifiques
        pass
