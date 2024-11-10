# from flask import Flask
# from flask_socketio import SocketIO

# # Crée l'application Flask et initialise SocketIO si nécessaire
# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'votre_cle_secrète'

#     # Initialise SocketIO si tu l'utilises
#     socketio = SocketIO(app)

#     # Ensuite, tu peux importer tes routes et sockets ici
#     from app import routes, sockets

#     return app
# from flask import Flask
# from flask_socketio import SocketIO

# socketio = SocketIO()  # Création de l'instance de SocketIO

# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'your_secret_key'

#     # Enregistrer les routes et les sockets après la création de l'application
#     with app.app_context():
#         from . import routes  # Import des routes
#         from . import sockets  # Import des sockets

#     socketio.init_app(app)  # Associer SocketIO à l'application Flask
#     return app

from flask import Flask
from flask_socketio import SocketIO

# Déclarez socketio en dehors de create_app pour en faire une variable globale
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Enregistrez les routes et les sockets après la création de l'application
    with app.app_context():
        from . import routes  # Importer les routes
        from . import sockets  # Importer les sockets

    # Associez l'instance SocketIO à l'application Flask
    socketio.init_app(app)
    return app
