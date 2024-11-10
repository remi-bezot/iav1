class Agent:
    def __init__(self, name, model_type):
        self.name = name
        self.model_type = model_type
        self.model = None  # Le modèle sera chargé ici (DQN, GPT-2)

    def train(self, data):
        """Entraîne le modèle avec des données spécifiques."""
        pass  # Ajouter la logique de formation ici

class Alice(Agent):
    def __init__(self):
        super().__init__("Alice", "DQN")

class Bob(Agent):
    def __init__(self):
        super().__init__("Bob", "GPT-2")

class Eve(Agent):
    def __init__(self):
        super().__init__("Eve", "GPT-2")
