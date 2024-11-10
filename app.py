from flask import Flask, jsonify, render_template, request, Response
from flask_socketio import SocketIO
from export_utils import export_teams, export_languages
import threading
import queue
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Queue pour la communication entre Flask et l'interface
ui_queue = queue.Queue()

# Variable globale pour suivre l'état de l'entraînement
is_training = False

def train():
    global is_training
    if not is_training:
        is_training = True
        print("Entraînement démarré...")
        socketio.emit('message', {'data': 'Entraînement démarré...'})
        time.sleep(5)  # Simule l'entraînement pendant 5 secondes
        is_training = False
        socketio.emit('message', {'data': 'Entraînement terminé !'})
        print("Entraînement terminé.")

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/start_training', methods=['POST'])
def start_training_route():
    global is_training
    if not is_training:
        training_thread = threading.Thread(target=train)
        training_thread.start()
        return jsonify({'response': 'Entraînement lancé !'})
    else:
        return jsonify({'response': 'L’entraînement est déjà en cours.'})

if __name__ == '__main__':
    socketio.run(app, debug=True, threaded=True)
