# from app import app  # Assure-toi que 'app' est bien importé
# from flask import request, jsonify, current_app as app

# @app.route('/execute-command', methods=['POST'])
# def execute_command():
#     data = request.get_json()
#     command = data.get('command')
#     if command:
#         response = "Réponse à la commande: " + command  # Exemple de réponse
#         return jsonify({'response': response})
#     else:
#         return jsonify({'error': 'Commande invalide'}), 400


# from flask import request, jsonify, render_template, current_app as app

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/execute-command', methods=['POST'])
# def execute_command():
#     data = request.get_json()
#     command = data.get('command')
#     if command:
#         response = "Réponse à la commande: " + command  # Exemple de réponse
#         return jsonify({'response': response})
#     else:
#         return jsonify({'error': 'Commande invalide'}), 400


# from flask import request, jsonify, render_template, current_app as app

# @app.route('/')
# def index():
#     return render_template('index.html')
# @app.route('/execute-command', methods=['POST'])
# def execute_command():
#     data = request.get_json()
#     command = data.get('command')
#     if command == "start":
#         # Insérer ici la logique pour initialiser les processus IA
#         response = "Les IA sont en cours de démarrage..."
#         return jsonify({'response': response})
#     elif command:
#         response = "Réponse à la commande: " + command
#         return jsonify({'response': response})
#     else:
#         return jsonify({'error': 'Commande invalide'}), 400



from app import app
from flask import render_template
import json
from app.ai.dqn import DQNAgent
from app.ai.gpt2 import GPT2Agent
from app.export.export_language import export_languages
from app.export.export_statistics import export_statistics

@app.route('/')
def index():
    dqn_agent = DQNAgent()
    gpt2_agent = GPT2Agent()
    dqn_response = dqn_agent.predict([0, 0, 0, 0])
    gpt2_response = gpt2_agent.generate("Translate 'Hello World' into French.")

    # Charger les données des équipes et des langues depuis les fichiers JSON
    with open('data/teams_data.json') as f:
        teams_data = json.load(f)

    with open('data/language_data.json') as f:
        languages_data = json.load(f)

    return render_template(
        'index.html',
        dqn_response=dqn_response,
        gpt2_response=gpt2_response,
        teams_data=teams_data,
        languages_data=languages_data
    )

@app.route('/export/languages')
def export_languages_route():
    languages = export_languages()
    return render_template('export.html', languages=languages)

@app.route('/export/statistics')
def export_statistics_route():
    statistics = export_statistics("DQN", 0.95)
    return render_template('export.html', statistics=statistics)
