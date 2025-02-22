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
    users[data] = request.sid
    sys.stdout.flush()

@socket.on('new_message')
def handle_new_message(data):
    data["message"] =  asyncio.run(translate_text(data["message"], "tamil"))
    for user in users:
        if users[user] == request.sid:
            data["user"] = user
    emit('chat', data, broadcast=True)
    sys.stdout.flush()