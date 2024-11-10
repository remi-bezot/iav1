import tkinter as tk

def create_button(root, text, command, **options):
    """
    Crée un bouton tkinter avec des options de configuration supplémentaires.
    Args:
        root: Le widget parent.
        text: Le texte du bouton.
        command: La commande à exécuter lorsque le bouton est cliqué.
        **options: Autres options pour configurer le bouton.
    Returns:
        tk.Button: Le bouton tkinter configuré.
    """
    button = tk.Button(root, text=text, command=command, **options)
    return button
