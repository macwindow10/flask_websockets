from gevent import monkey

monkey.patch_all()

from gevent.pywsgi import WSGIServer
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        if data == 'close':
            break
        ws.send(data)


@sock.route('/Fn1')
def fn1(ws):
    # while True:
    data = ws.receive()
    ws.send(data)


if __name__ == '__main__':
    print("Server starting")
    WSGIServer(('127.0.0.1', 5000), app).serve_forever()
