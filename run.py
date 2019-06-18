from flask import Flask, render_template
from flask_socketio import SocketIO, send
from textblob import TextBlob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    text = msg["data"]
    send({"from": "me", "data": text})
    blob = TextBlob(u'{}'.format(text))
    send({"from": "bot", "data": str(blob.translate(to="vi"))})

if __name__ == '__main__':
    socketio.run(app)
    app.run()
