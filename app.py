# # # from flask import Flask, render_template

# # # app = Flask(__name__)

# # # @app.route('/')
# # # def home():
# # #     return render_template('index.html')

# # # if __name__ == '__main__':
# # #     app.run(debug=True)

# # # import threading

# # # def start_training():
# # #     def train():
# # #         # Ton code d'entraînement ici
# # #         train_models()

# # #     # Démarre l'entraînement sur un thread séparé
# # #     training_thread = threading.Thread(target=train)
# # #     training_thread.start()



# # from flask import Flask, render_template
# # import threading
# # import queue

# # app = Flask(__name__)

# # # Queue pour la communication entre Flask et Tkinter
# # ui_queue = queue.Queue()

# # def train():
# #     # Ton code d'entraînement ici
# #     # Par exemple, simulateur d'entraînement
# #     print("Entraînement démarré...")
# #     # Une fois l'entraînement terminé, tu envoies un message à Tkinter
# #     ui_queue.put("Entraînement terminé !")

# # @app.route('/')
# # def home():
# #     return render_template('index.html')

# # @app.route('/start_training')
# # def start_training():
# #     # Démarre l'entraînement sur un thread séparé
# #     training_thread = threading.Thread(target=train)
# #     training_thread.start()
# #     return "Entraînement lancé !"

# # if __name__ == '__main__':
# #     app.run(debug=True)



# # from flask import Flask, jsonify
# # import threading
# # import queue

# # # Initialisation de Flask
# # app = Flask(__name__)

# # # Queue pour la communication entre Flask et Tkinter
# # ui_queue = queue.Queue()

# # def train():
# #     # Simule l'entraînement ici (par exemple un simple délai)
# #     print("Entraînement démarré...")
# #     # Une fois l'entraînement terminé, envoie un message à la queue
# #     ui_queue.put("Entraînement terminé !")

# # @app.route('/')
# # def home():
# #     return "Serveur Flask fonctionne !"

# # @app.route('/start_training')
# # def start_training():
# #     # Démarre l'entraînement dans un thread séparé
# #     training_thread = threading.Thread(target=train)
# #     training_thread.start()
# #     return "Entraînement lancé !"

# # if __name__ == '__main__':
# #     app.run(debug=True, threaded=True)  # Assure-toi que Flask accepte plusieurs connexions

# from flask import Flask, render_template
# import os
# import sys
# from export.export_language import export_languages
# import threading
# import queue
# sys.path.append(os.path.join(os.path.dirname(__file__), '../export'))

# app = Flask(__name__)

# # Queue pour la communication entre Flask et Tkinter
# ui_queue = queue.Queue()

# def train():
#     # Simule l'entraînement ici (par exemple un simple délai)
#     print("Entraînement démarré...")
#     # Une fois l'entraînement terminé, envoie un message à la queue
#     ui_queue.put("Entraînement terminé !")

# @app.route('/')
# def home():
#     # Affiche index.html
#     return render_template('index.html')

# @app.route('/export_language')
# def export_languages_route():
#     return export_languages()  # Appelle la fonction dans export_language.py

# @app.route('/export-statistics')
# def export_statistics_route():
#     # Code pour exporter les statistiques
#     return "Export des statistiques"


# @app.route('/start_training')
# def start_training():
#     # Démarre l'entraînement dans un thread séparé
#     training_thread = threading.Thread(target=train)
#     training_thread.start()
#     return "Entraînement lancé !"

# if __name__ == '__main__':
#     app.run(debug=True, threaded=True)  # Assure-toi que Flask accepte plusieurs connexions


# from flask import Flask, render_template, request, jsonify

from flask import Flask, jsonify, send_file, Response, render_template
from export_utils import export_teams, export_languages
from flask_socketio import SocketIO, emit
import os
import sys
import threading
import time
import queue
sys.path.append(os.path.join(os.path.dirname(__file__), '../export'))

app = Flask(__name__)
socketio = SocketIO(app)

# Queue pour la communication entre Flask et l'interface
ui_queue = queue.Queue()

# Variable globale pour suivre l'état de l'entraînement
is_training = False

def train():
    print("Entraînement démarré...")
    socketio.emit('message', {'data': 'Entraînement démarré...'})
    time.sleep(5)  # Simule l'entraînement pendant 5 secondes
    socketio.emit('message', {'data': 'Entraînement terminé !'})
    print("Entraînement terminé.")

@app.route('/')
def home():
    teams_data = [
        {"team_name": "Equipe A", "members": 5},
        {"team_name": "Equipe B", "members": 4}
    ]
    languages_data = [
        {"code": "en", "name": "Anglais"},
        {"code": "fr", "name": "Français"}
    ]
    return render_template('index.html', teams_data=teams_data, languages_data=languages_data)

@app.route('/export/teams')
def export_teams_route():
    csv_data = export_teams()
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=teams.csv"}
    )

@app.route('/export/languages')
def export_languages_route():
    csv_data = export_languages()
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=languages.csv"}
    )

@app.route('/export-statistics')
def export_statistics_route():
    return "Export des statistiques"

@app.route('/start_training', methods=['POST'])
def start_training():
    global is_training
    if not is_training:
        training_thread = threading.Thread(target=train)
        training_thread.start()
        return jsonify({'response': 'Entraînement lancé !'})
    else:
        return jsonify({'response': 'L’entraînement est déjà en cours.'})

@app.route('/stop_training', methods=['POST'])
def stop_training():
    global is_training
    if is_training:
        is_training = False
        return jsonify({'response': 'Entraînement arrêté.'})
    else:
        return jsonify({'response': 'Aucun entraînement en cours.'})

@app.route('/execute-command', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command', '').lower()

    # Exécution de la commande
    if command == "start" or command == "start training":
        return start_training()
    elif command == "stop" or command == "stop training":
        return stop_training()
    else:
        return jsonify({'response': "Commande non reconnue."})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
