class SpecialString:
  def __init__(self, content):
    self.content = content

  def __gt__(self, other):
    for index in range(len(other.content)+1):
      print("index:"+str(index)+"\n")
      result = other.content[:index] + ">" + self.content
      result += ">" + other.content[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")

# spam > eggs
# index:0
#
# >spam>eggs
# index:1
#
# e>spam>ggs
# index:2
#
# eg>spam>gs
# index:3
#
# egg>spam>s
# index:4
#
# eggs>spam>