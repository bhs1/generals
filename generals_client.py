import socketio
import requests
import certifi
import ssl


s = requests.Session()
s.verify = certifi.where()
sio = socketio.Client(logger=True, engineio_logger=True, ssl_verify=True, http_session=s)

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

@sio.event
def message(data):
    print('I received a message!')

@sio.event
def connect_error(data):
    print(data)
    print("The connection failed!")

sio.connect('http://botws.generals.io')
sio.wait()
