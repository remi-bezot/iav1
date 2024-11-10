import tkinter as tk
import threading
from interface.ui_main import App
from simulation.training_simulation import train_models
from flask_socketio import SocketIO
from app import app  # Importer l'application Flask définie

# Lancer l'entraînement (simulations)
def start_training():
    train_models()

# Démarrer Flask dans un thread séparé
def run_flask():
    socketio = SocketIO(app)
    socketio.run(app, debug=True, use_reloader=False)  # Démarre Flask sans recharger

# Code principal
if __name__ == "__main__":
    # Crée l'interface Tkinter
    root = tk.Tk()
    app_gui = App(root)

    # Démarrer Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Lancer l'interface graphique Tkinter
    root.mainloop()
