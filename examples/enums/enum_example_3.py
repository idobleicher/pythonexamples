from enum import Enum

class Mood(Enum):
    FUNKY = 1
    HAPPY = 3

    def describe(self):
        # self is the member here
        return self.name, self.value

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        # cls here is the enumeration
        return cls.HAPPY




happy_enum_tuple= Mood.HAPPY.describe()
print(happy_enum_tuple)
#('HAPPY', 3)

print(str(Mood.FUNKY))
#'my custom str! 1'


print(Mood.favorite_mood())
#my custom str! 3
