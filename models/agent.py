
import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

class DQNAgent:
    def __init__(self):
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(24, activation="relu", input_shape=(4,)),
            tf.keras.layers.Dense(24, activation="relu"),
            tf.keras.layers.Dense(2, activation="linear")
        ])
        model.compile(optimizer="adam", loss="mse")
        return model

    def predict(self, state):
        return self.model.predict(state)

    def train_on_batch(self, states, q_values):
        return self.model.train_on_batch(states, q_values)

class GPT2Agent:
    def __init__(self):
        self.model = TFGPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="tf")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0])
