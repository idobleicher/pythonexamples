from flask import Flask

app = Flask(__name__)

#You can add variable sections to a URL by marking sections with <variable_name>.
# Your function then receives the <variable_name> as a keyword argument.
# Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

#Converter types:
#
# string	(default) accepts any text without a slash
# int	accepts positive integers
# float	accepts positive floating point values
# path	like string but also accepts slashes
# uuid	accepts UUID strings


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

if __name__ == '__main__':
    app.run(host='0.0.0.0')