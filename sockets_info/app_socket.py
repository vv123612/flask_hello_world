from flask import Flask
from flask import request
import sys, os, platform
import datetime
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)

def get_env():
    return [("<p>"+key+" = "+value+"<p>") for key,value in sorted(dict(os.environ).items())]


def info():
    # print(request.data)
    # print(request.namespace.socket.sessid)
    # return str(request.data)
    # return "Hello World!"


    s='\n'

    # <p>client socket - {request.namespace.socket.sessid}</p>

    return f'''
    <p>Hello World! </p>
    <p>P{datetime.datetime.now()} </p>
    <p>IP {request.remote_addr}</p>
    <p>-----------------------------------------</p>
    <p>os.name: {os.name}</p>
    <p>platform.system(): {platform.system()}</p>
    <p>platform.release(): ', {platform.release()}</p>
    <p>executable: ', {sys.executable}</p>

    <p>Packages:
    <p>{s.join(sys.path)}</p>
    
    -----------------------------------------
    <p>os.environ).items() </p>
    <p>{s.join(get_env())}</p>
    '''


@socketio.on('connect')
def onConnect():
    print(request.namespace.socket.sessid)


@app.route('/')
def hello_world():
    # request.data
    # return 'Hello World!'
    # return f'''Hello World! \n IP {request.remote_addr}'''
    return info()

if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
    socketio.run(app, debug=True, host='0.0.0.0')
