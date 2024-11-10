# import tkinter as tk
# from tkinter import messagebox
# from simulation.training_simulation import train_models

# class App:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("AI Communication Project")
        
#         self.start_button = tk.Button(self.root, text="Start Training", command=self.start_training)
#         self.start_button.pack(pady=10)
        
#         self.stop_button = tk.Button(self.root, text="Stop Training", command=self.stop_training)
#         self.stop_button.pack(pady=10)

#     def start_training(self):
#         train_models()
#         messagebox.showinfo("Training", "Training Started")

#     def stop_training(self):
#         messagebox.showinfo("Training", "Training Stopped")



# import tkinter as tk
# from tkinter import messagebox
# from simulation.training_simulation import train_models
# import threading

# class App:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("AI Communication Project")
        
#         self.start_button = tk.Button(self.root, text="Start Training", command=self.start_training)
#         self.start_button.pack(pady=10)
        
#         self.stop_button = tk.Button(self.root, text="Stop Training", command=self.stop_training)
#         self.stop_button.pack(pady=10)
        
#         self.training_thread = None

#     def start_training(self):
#         try:
#             self.training_thread = threading.Thread(target=train_models)
#             self.training_thread.start()
#             messagebox.showinfo("Training", "Training Started")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred while starting the training: {e}")

#     def stop_training(self):
#         if self.training_thread and self.training_thread.is_alive():
#             # Implémente une méthode pour arrêter le thread ici si possible
#             messagebox.showinfo("Training", "Training Stopped")
#         else:
#             messagebox.showinfo("Training", "No training is running")

# # Lancer l'application Tkinter
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
from simulation.training_simulation import train_models
import threading

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Communication Project")
        
        self.start_button = tk.Button(self.root, text="Start Training", command=self.start_training)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop Training", command=self.stop_training)
        self.stop_button.pack(pady=10)
        
        self.training_thread = None
        self.stop_flag = threading.Event()

    def start_training(self):
        try:
            # Reset the stop flag before starting
            self.stop_flag.clear()
            self.training_thread = threading.Thread(target=self.run_training)
            self.training_thread.start()
            messagebox.showinfo("Training", "Training Started")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while starting the training: {e}")

    def run_training(self):
        # Passe le flag pour permettre l'arrêt
        train_models(self.stop_flag)

    def stop_training(self):
        if self.training_thread and self.training_thread.is_alive():
            self.stop_flag.set()  # Demande d'arrêt
            messagebox.showinfo("Training", "Training Stopping... Please wait")
        else:
            messagebox.showinfo("Training", "No training is running")

# Lancer l'application Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
