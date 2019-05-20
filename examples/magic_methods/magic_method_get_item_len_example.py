import random

class VagueList:
  def __init__(self, content):
    self.content = content

  def __getitem__(self, index):
    return self.content[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.content)*2)


vague_list = VagueList(["A", "B", "C", "D", "E"])

print(len(vague_list))
#10 - random

print(len(vague_list))
#2 - random

print(vague_list[2])
#B-random
print(vague_list[2])
#C-random