from examples.simple_game_exa.Goblin import *

goblin = Goblin("Gobbly")


def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)



examine("d")

