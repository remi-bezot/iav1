# from app import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)


# from app import create_app, socketio

# app = create_app()

# if __name__ == "__main__":
#     socketio.run(app, debug=True)
# from app import create_app, socketio

# app = create_app()

# if __name__ == "__main__":
#     socketio.run(app, debug=True)



# import tkinter as tk
# from interface.ui_main import App
# from simulation.training_simulation import train_models
# from models.gan_model import GanModel

# def start_training():
#     train_models()

# def stop_training():
#     # Arrêter l'entraînement et afficher les résultats
#     pass

# if __name__ == "__main__":
#     # Crée l'interface
#     root = tk.Tk()
#     app = App(root)

#     # Lancer les simulations et l'entraînement au démarrage
#     start_training()

#     # Lancer l'interface graphique
#     root.mainloop()


# import tkinter as tk
# import threading
# from interface.ui_main import App
# from simulation.training_simulation import train_models
# from models.gan_model import GanModel
# from app import app  # Assure-toi que Flask est bien importé

# def start_training():
#     train_models()

# def stop_training():
#     # Arrêter l'entraînement et afficher les résultats
#     pass

# def run_flask():
#     app.run(debug=True, use_reloader=False)  # Démarre le serveur Flask, en désactivant le reloader

# if __name__ == "__main__":
#     # Crée l'interface Tkinter
#     root = tk.Tk()
#     app_gui = App(root)

#     # Lancer les simulations et l'entraînement au démarrage
#     start_training()

#     # Démarrer Flask dans un thread séparé
#     flask_thread = threading.Thread(target=run_flask)
#     flask_thread.start()

#     # Lancer l'interface graphique Tkinter
#     root.mainloop()



import tkinter as tk
import threading
from app import app  # Assure-toi que 'app' est bien importé depuis ton fichier Flask
from simulation.training_simulation import train_models
from interface.ui_main import App

# Lancer l'entraînement (simulations)
def start_training():
    train_models()

# Démarrer Flask dans un thread séparé
def run_flask():
    app.run(debug=True, use_reloader=False)  # Démarre Flask sans reloader

# Code principal
if __name__ == "__main__":
    # Crée l'interface Tkinter
    root = tk.Tk()
    app_gui = App(root)  # Assure-toi que tu as bien défini ta classe 'App' dans le module 'interface.ui_main'

    # Lancer les simulations et l'entraînement au démarrage
    start_training()

    # Démarrer Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Lancer l'interface graphique Tkinter
    root.mainloop()
