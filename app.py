from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'''Hello World! \n IP {request.remote_addr}'''

if __name__ == '__main__':
    app.run(debug=True)
