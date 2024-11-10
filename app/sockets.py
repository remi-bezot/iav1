# from app import socketio

# @socketio.on('message')
# def handle_message(message):
#     print(f'Reçu: {message}')
#     socketio.send('Réponse du serveur: Message reçu')


from . import socketio

@socketio.on('connect')
def handle_connect():
    print("Client connecté")
