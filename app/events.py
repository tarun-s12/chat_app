from .extensions import socket
from .translate import translate_text
import asyncio
import sys
from flask_socketio import emit
from flask import request

users = {}

@socket.on('connect')
def handle_connect():
    print('Client connected')
    sys.stdout.flush()

@socket.on('name')
def handle_name(data):
    users[request.sid] = {'name': data['name'], 'language': data['language']}

@socket.on('new_message')
def handle_new_message(data):
    sender = users.get(request.sid)
    if sender:
        message = data.get('message')
        for sid, user in users.items():
            translated_message = asyncio.run(translate_text(message, user['language']))
            emit('chat', {'user': sender['name'], 'message': translated_message}, room=sid)