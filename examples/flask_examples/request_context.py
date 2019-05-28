from flask import Flask ,request

app = Flask(__name__)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


with app.test_request_context('/?name=Peter'):
    assert request.path == '/'
    assert request.args['name'] == 'Peter'