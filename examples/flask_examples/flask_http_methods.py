from flask import Flask ,request

app = Flask(__name__)

def do_the_login():
    return "do the login"

def show_the_login_form():
    return "show_the_login_form"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
