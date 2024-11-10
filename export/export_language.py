# from app.utils import load_data
# import json  # Assure-toi que json est importé

# def export_languages():
#     data = load_data("data/language_data.json")
#     # Processus d'exportation de données
#     with open("exported_language_data.json", "w") as file:
#         json.dump(data, file, indent=4)
#     return data  # Assure-toi de renvoyer la donnée si nécessaire

# import os
# from flask import Flask, render_template, send_from_directory

# app = Flask(__name__)

# # Route pour servir les fichiers du dossier 'export' à la racine
# @app.route('/export_language')
# def export_languages():
#     export_path = os.path.join(os.getcwd(), 'export')
#     filename = 'export_language.py'  # Remplace par le nom du fichier réel
    
#     if os.path.exists(os.path.join(export_path, filename)):
#         return send_from_directory(export_path, filename)
#     else:
#         return "Le fichier demandé n'existe pas.", 404
#     # Tu peux retourner un fichier spécifique du dossier export, par exemple:
#     # return send_from_directory(export_path, 'ton_fichier_a_exporter.ext')

# @app.route('/')
# def home():
#     return render_template('index.html')


# export_utils.py

import csv
from io import StringIO

def export_teams():
    teams = [
        {"id": 1, "name": "Team A"},
        {"id": 2, "name": "Team B"},
        # Ajoutez vos équipes ici
    ]
    return generate_csv(teams, ["id", "name"])

def export_languages():
    languages = [
        {"id": 1, "name": "English"},
        {"id": 2, "name": "French"},
        # Ajoutez vos langues ici
    ]
    return generate_csv(languages, ["id", "name"])

def generate_csv(data, headers):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
    output.seek(0)
    return output.getvalue()
