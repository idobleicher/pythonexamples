
#  the control is being passed back and forth
#  Those are coroutines.
#  They can be used for all kinds of cool things like asynch IO and similar.
#
# Think of it like this, with a generator and no send, it's a one way street
#
# ==========       yield      ========
# Generator |   ------------> | User |
# ==========                  ========
# But with send, it becomes a two way street
#
# ==========       yield       ========
# Generator |   ------------>  | User |
# ==========    <------------  ========
#                   send
# Which opens up the door to the user customizing the generators behavior on the fly and the generator responding to the user.




def coroutine():
    for i in range(1, 10):
        res=yield i
        print("From generator {}".format(res))


c = coroutine()
c.send(None)

try:
    while True:
        val = c.send(100)
        print("From user {}".format(val))
except StopIteration: pass

# From generator 100
# From user 2
# From generator 100
# From user 3
# From generator 100
# From user 4
# From generator 100
# From user 5
# From generator 100
# From user 6
# From generator 100
# From user 7
# From generator 100
# From user 8
# From generator 100
# From user 9
# From generator 100
