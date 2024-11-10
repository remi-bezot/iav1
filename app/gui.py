# import tkinter as tk
# import requests
# import queue

# # Queue pour recevoir les messages de Flask
# ui_queue = queue.Queue()

# def start_training():
#     # Appelle l'API Flask pour démarrer l'entraînement
#     response = requests.get('http://127.0.0.1:5000/start_training')
#     print(response.text)

# def update_ui():
#     try:
#         # Essayer de récupérer un message de la queue
#         message = ui_queue.get_nowait()
#         # Mettre à jour l'interface avec le message
#         message_label.config(text=message)
#     except queue.Empty:
#         pass

#     # Mettre à jour l'interface toutes les 100 ms
#     root.after(100, update_ui)

# # Configuration de la fenêtre Tkinter
# root = tk.Tk()
# root.title("Interface d'Entraînement")

# message_label = tk.Label(root, text="Lancement de l'entraînement...")
# message_label.pack()

# start_button = tk.Button(root, text="Démarrer l'Entraînement", command=start_training)
# start_button.pack()

# # Lancer la mise à jour de l'interface
# root.after(100, update_ui)

# root.mainloop()




import tkinter as tk
import requests
import queue
import threading

# Queue pour recevoir les messages de Flask
ui_queue = queue.Queue()

def start_training():
    # Fonction dans un thread séparé pour éviter de bloquer l'interface Tkinter
    def run():
        response = requests.get('http://127.0.0.1:5000/start_training')
        print(response.text)
        ui_queue.put("Entraînement démarré...")
    threading.Thread(target=run).start()

def update_ui():
    try:
        # Essayer de récupérer un message de la queue
        message = ui_queue.get_nowait()
        # Mettre à jour l'interface avec le message
        message_label.config(text=message)
    except queue.Empty:
        pass

    # Mettre à jour l'interface toutes les 100 ms
    root.after(100, update_ui)

# Configuration de la fenêtre Tkinter
root = tk.Tk()
root.title("Interface d'Entraînement")

message_label = tk.Label(root, text="Lancement de l'entraînement...")
message_label.pack()

start_button = tk.Button(root, text="Démarrer l'Entraînement", command=start_training)
start_button.pack()

# Lancer la mise à jour de l'interface
root.after(100, update_ui)

root.mainloop()
