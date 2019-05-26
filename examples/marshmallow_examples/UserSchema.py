from marshmallow import Schema, fields

#Create a schema by defining a class with variables mapping attribute names to Field objects.
class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()