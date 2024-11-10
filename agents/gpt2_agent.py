from transformers import GPT2LMHeadModel, GPT2Tokenizer
import tensorflow as tf
from typing import Union

class GPT2Agent:
    def __init__(self, use_tf: bool = False):
        """
        Classe GPT-2 pour la génération de texte.

        Args:
            use_tf (bool): Utiliser le modèle TensorFlow (True) ou PyTorch (False). Par défaut, PyTorch.
        """
        self.use_tf = use_tf
        if use_tf:
            self.model = TFGPT2LMHeadModel.from_pretrained('gpt2')
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        else:
            self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
            self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def generate(self, prompt: str, max_length: int = 100, num_return_sequences: int = 1) -> str:
        """
        Génère du texte à partir d'un prompt donné.

        Args:
            prompt (str): Le texte d'entrée à partir duquel générer la suite.
            max_length (int): La longueur maximale du texte généré.
            num_return_sequences (int): Le nombre de séquences de retour.

        Returns:
            str: Le texte généré par le modèle.
        """
        inputs = self.tokenizer.encode(prompt, return_tensors='tf' if self.use_tf else 'pt')
        outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=num_return_sequences)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Exemple d'utilisation
if __name__ == "__main__":
    gpt2_agent = GPT2Agent(use_tf=False)  # Choix entre TensorFlow ou PyTorch
    prompt = "Once upon a time"
    generated_text = gpt2_agent.generate(prompt)
    print(generated_text)
