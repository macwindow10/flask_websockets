from gevent import monkey

monkey.patch_all()

from gevent.pywsgi import WSGIServer
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)

checker = False


@sock.route('/Function_1')
def function_1(ws):
    print('function_1')
    data = ws.receive()
    # access global variabler
    global checker
    checker = False


@sock.route('/Function_2_3')
def function_2_3(ws):
    print('function_2_3')
    data = ws.receive()
    # access global variabler
    global checker
    checker = True


if __name__ == '__main__':
    print("Server starting on 192.168.100.246:5000")
    WSGIServer(('192.168.100.246', 5000), app).serve_forever()
