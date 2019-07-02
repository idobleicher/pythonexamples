import json
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

y = json.loads(data)
print(y)
# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('NA', d.keys())(*d.values()))
print (x.name, x.hometown.name, x.hometown.id)

def _json_object_hook(d): return namedtuple('NA', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
z = json2obj(data)
print (z.name, z.hometown.name, z.hometown.id)


