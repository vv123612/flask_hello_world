from flask import Flask
from flask import request
import sys, os, platform
import datetime


app = Flask(__name__)

def get_env():
    return [("<p>"+key+" = "+value+"<p>") for key,value in dict(os.environ).items()]


def info():
    s='\n'

    return f'''
    <p>Hello World! </p>
    <p>{datetime.datetime.now()} </p>
    <p>{request.headers}<p>
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



@app.route('/')
def hello_world():
    # return 'Hello World!'
    # return f'''Hello World! \n IP {request.remote_addr}'''
    return info()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0')
