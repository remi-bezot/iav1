import tkinter as tk
from interface.ui_main import App
from simulation.training_simulation import train_models
from models.gan_model import GanModel

def start_training():
    train_models()

def stop_training():
    # Arrêter l'entraînement et afficher les résultats
    pass

if __name__ == "__main__":
    # Crée l'interface
    root = tk.Tk()
    app = App(root)

    # Lancer les simulations et l'entraînement au démarrage
    start_training()

    # Lancer l'interface graphique
    root.mainloop()
