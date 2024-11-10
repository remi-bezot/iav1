import json

def load_data(file_path):
    """Charge les données à partir d'un fichier JSON."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_data(data, file_path):
    """Sauvegarde les données dans un fichier JSON."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
