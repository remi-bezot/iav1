from models.dqn_agent import DQNAgent
from models.gan_model import GanModel
import numpy as np

def train_models():
    # Paramètres d'exemple
    state_size = 4
    action_size = 2
    agent = DQNAgent(state_size, action_size)
    
    # Entraînement simple
    for e in range(100):
        state = np.random.random((1, state_size))
        action = agent.act(state)
        reward = np.random.random()
        next_state = np.random.random((1, state_size))
        done = e == 99
        agent.remember(state, action, reward, next_state, done)
        agent.replay(32)
        if done:
            print(f"Episode {e+1}: Recompense {reward}")
