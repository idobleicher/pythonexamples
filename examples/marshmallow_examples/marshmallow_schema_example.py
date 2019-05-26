from marshmallow import Schema, fields
from datetime import date

# Marshmallow is an ORM (Object Relational Mapper)/ODM (Object Document Mapper)/framework-agnostic
# library for converting complex datatypes, such as objects, to and from native Python datatypes.


from marshmallow import Schema, fields, pprint

class ArtistSchema(Schema):
    name = fields.Str()

class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

bowie = dict(name='David Bowie')
album = dict(artist=bowie, title='Hunky Dory', release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result.data, indent=2)
# { 'artist': {'name': 'David Bowie'},
#   'release_date': '1971-12-17',
#   'title': 'Hunky Dory'}