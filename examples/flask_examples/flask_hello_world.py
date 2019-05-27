from flask import Flask

#C:\git-views\pythonexamples\examples\flask_examples>set FLASK_APP=flask_hello_world.py
#C:\git-views\pythonexamples\examples\flask_examples>flask run
#OR
#C:\git-views\pythonexamples\examples\flask_examples>python -m flask run

#we imported the Flask class. An instance of this class will be our WSGI application

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' #when in debug we can modify it and see automatic changes on page - automatic reloading