
#Serializing Objects (“Dumping”)

#Serialize objects by passing them to your schema’s dump method,
# which returns the formatted result (as well as a dictionary of validation
# errors, which we’ll revisit later).

from marshmallow import pprint
from examples.marshmallow_examples.User import User
from examples.marshmallow_examples.UserSchema import UserSchema


user = User(name="Monty", email="monty@python.org")

schema = UserSchema()

result = schema.dump(user)
pprint(result.data)
# {"name": "Monty",
#  "email": "monty@python.org",
#  "created_at": "2014-08-17T14:54:16.049594+00:00"}

#Filtering output¶
summary_schema = UserSchema(only=('name', 'email'))
pprint(summary_schema.dump(user).data)
#{'email': 'monty@python.org', 'name': 'Monty'}