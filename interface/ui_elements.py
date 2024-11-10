import tkinter as tk

def create_button(root, text, command):
    button = tk.Button(root, text=text, command=command)
    return button
