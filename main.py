from app import create_app, socket

app = create_app()
socket.run(app)