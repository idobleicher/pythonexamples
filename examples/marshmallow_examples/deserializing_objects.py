#Deserializing Objects (“Loading”)

from marshmallow import Schema, fields, post_load , pprint
from examples.marshmallow_examples.User import User
from examples.marshmallow_examples.UserSchema import UserSchema

user_data = {
    'created_at': '2014-08-11T05:26:03.869245',
    'email': u'ken@yahoo.com',
    'name': u'Ken'
}
schema = UserSchema()

#By default, load will return a dictionary of field names mapped to the deserialized values.
result = schema.load(user_data)
pprint(result.data)
# {'name': 'Ken',
#  'email': 'ken@yahoo.com',
#  'created_at': datetime.datetime(2014, 8, 11, 5, 26, 3, 869245)},



#Deserializing to Objects
#In order to deserialize to an object, define a method of your Schema and decorate it with post_load.
# The method receives a dictionary of deserialized data as its only parameter.



class UserSchema2(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)

print("-----------------------------")
#Now, the load method will return a User object.
user_data = {
    'name': 'Ronnie',
    'email': 'ronnie@stones.com'
}
schema = UserSchema2()
result = schema.load(user_data)
print(result.data ) # => <User(name='Ronnie')>
#<User(name='Ronnie')>
