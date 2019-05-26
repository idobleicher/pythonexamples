from examples.generators.is_prime import is_prime

#In PEP 342, support was added for passing values into generators. PEP 342 gave generators the power to yield a value (as before),
# receive a value, or both yield a value and receive a (possibly different) value in a single statement.


#To illustrate how values are sent to a generator, let's return to our prime number example.
# This time, instead of simply printing every prime number greater than number, #
# we'll find the smallest prime number greater than successive powers of a number (i.e. for 10,
# we want the smallest prime greater than 10, then 100, then 1000,

def get_primes(number):
    print ("init get_prime with" , str(number))
    while True:
        if is_prime(number):
            #return number is following the send value
            number = yield number
        number += 1




def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)

    # Using send to start a generator - execute the code from the first line of the generator function up to the first yield statement
    prime_generator.send(None)

    for power in range(iterations):
        print("power:" , str(power))
        print(prime_generator.send(base ** power)) #sending number


print_successive_primes(iterations=3)
#
# init get_prime with 10
# power: 0
# 2 - smallest prime after 10^0
# power: 1
# 11- smallest prime after 10^1
# power: 2
# 101-- smallest prime after 10^2