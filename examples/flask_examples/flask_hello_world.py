from flask import Flask



app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!' #when in debug we can modify it and see automatic changes on page - automatic reloading

if __name__ == '__main__':
    app.run(host='0.0.0.0')