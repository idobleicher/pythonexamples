from flask import Flask

#The canonical URL for the projects endpoint has a trailing slash.
# It’s similar to a folder in a file system.
# If you access the URL without a trailing slash, Flask redirects you to the canonical URL with the trailing slash.
#http://0.0.0.0:5000/projects -> #http://0.0.0.0:5000/projects/


#The canonical URL for the about endpoint does not have a trailing slash. It’s similar to the pathname of a file.
# Accessing the URL with a trailing slash produces a 404 “Not Found” error.
#http://0.0.0.0:5000/about - ok
#http://0.0.0.0:5000/about/ - 404

# This helps keep URLs unique for these resources, which helps search engines avoid indexing the same page twice.

app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(host='0.0.0.0')