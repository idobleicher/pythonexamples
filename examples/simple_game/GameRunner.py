from examples.simple_game.Goblin import *




def say(noun):
  return 'You said "{}"'.format(noun)


def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)


def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health -= 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else:
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg = "There is no {} here.".format(noun)
  return msg


verb_dictionary = {
  "say": say,
  "examine": examine,
  "hit": hit,
}


def get_input():
  command = input("Command: ").split()
  verb_word = command[0]
  if verb_word in verb_dictionary:
    verb = verb_dictionary[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))



def run_game():
  while True:
    get_input()



   #main

goblin = Goblin("Gobbly")

run_game()

# Command: say hi
# You said "hi"

# Command: examine goblin
# goblin
#  A foul creature


# Command: examine bla
# There is no bla here.

# Command: hit goblin
# You hit the goblin
