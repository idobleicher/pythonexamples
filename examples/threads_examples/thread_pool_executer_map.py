#Executor.map()

# Both executors have a common method – map().
# Like the built in function,
# the map method allows multiple calls to a provided function,
# passing each of the items in an iterable to that function.
#
# Except,# in this case, the functions are called concurrently.
# For multiprocessing, this iterable is broken into chunks and each of these chunks is passed to the function in separate processes.
# We can control the chunk size by passing a third parameter, chunk_size.
# By default the chunk size is 1.


import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()