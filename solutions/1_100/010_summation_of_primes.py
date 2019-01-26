
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


import math


def is_prime(number: int):
    limit = math.floor(math.sqrt(number)) + 1
    for i in range(2, limit):
        if number % i == 0:
            return False
    return True


def main(number: int):
    sum = 0

    if number % 2 == 0:
        sum += 2

    for i in range(3, number, 2):
        if is_prime(i):
            sum += i

    print(sum)


if __name__ == '__main__':
    main(2_000_000)
