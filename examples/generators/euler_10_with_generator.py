from examples.generators.is_prime import is_prime


#getting prime with generator
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
#
# get_prime_generator = get_primes(3)
# print(next(get_prime_generator))
# #3
# print(next(get_prime_generator))
# #5

def solve_euler_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

solve_euler_number_10()
#142913828922