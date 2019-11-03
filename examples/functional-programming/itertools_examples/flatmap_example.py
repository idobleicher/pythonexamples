
from itertools import chain


print("------------------------")
episodes = [
    {"id": 1, "topics": [1,2,3]},
    {"id": 2, "topics": [4,5,6]}
]

flattened_episodes = []
for episode in episodes:
    for topic in episode["topics"]:
        id = episode["id"]
        flattened_episodes.append({"id": id, "topic": topic})

for episode in flattened_episodes:
    print (episode)
print("------------------------")


#Using list comprehension
lattened_episodes2 = [{"id": episode["id"], "topic": topic}
                      for episode in episodes
                      for topic in episode["topics"]]

for episode in lattened_episodes2:
    print (episode)

print("------------------------")


#Using   flat map implemented with itertools chain.from_iterable + map

def flat(coll):
    """
    same as chain.from_iterable, common idiom for doing things
    like flat(map(...))

    :param coll: iterable of iterables to flatten
    :return: an flat iterable from the nested iterables
    """
    return chain.from_iterable(coll)


def flatmap(f, *iterables):
    """
    apply function to collection and flatten resulting iterable
    Example:

        iterables = ['a b c', 'd e f']
        f = str.split
        assert flatmap(f, iterables) == ['a', 'b', 'c', 'd', 'e', 'f']


    :param f: function to apply
    :param iterables: collections to apply to (same style as map)
    :return: flattened result of map(f, *colls)
    """
    return flat(map(f, *iterables))

flatmap_lambda = lambda episode: [{"id": episode["id"], "topic": topic} for topic in episode["topics"]]
flattened_episodes3 = flatmap(flatmap_lambda, episodes)
for episode in flattened_episodes3:
    print (episode)
