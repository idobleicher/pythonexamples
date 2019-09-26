from pluck import pluck, ipluck
from datetime import datetime

#  is the simplest way of plucking “fields” from an iterable of values.
# “Fields” are either item.field or item[field]. Pluck tries both,
# in that order. If nothing is found, and no default value is specified,
# it throws an exception.
#pluck(iterable, key)
#pluck(iterable, *keys)

dates = [
    datetime(2012, 10, 22, 12, 00),
    datetime(2012, 10, 22, 15, 14),
    datetime(2012, 10, 22, 21, 44),
        ]
print(pluck(dates, 'day'))
#[22, 22, 22]
print(pluck(dates, 'hour'))
#[12, 15, 21]

#It also works on dictionary-like access (__getitem__):
objects = [
    {'id': 282, 'name': 'Alice', 'age': 30, 'sex': 'female'},
    {'id': 217, 'name': 'Bob', 'age': 56},
    {'id': 328, 'name': 'Charlie', 'age': 56, 'sex': 'male'},
    ]
print(pluck(objects, 'name'))
#['Alice', 'Bob', 'Charlie']
print(pluck(objects, 'age'))
#[30, 56, 56]

#You can also combine these into a single pluck:
print(pluck(objects, 'name', 'age'))
#[('Alice', 30), ('Bob', 56), ('Charlie', 56)]