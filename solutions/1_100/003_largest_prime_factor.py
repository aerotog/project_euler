
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


import math


def is_prime(number: int):
    limit = math.floor(math.sqrt(number))+1
    for i in range(2, limit):
        if number % i == 0:
            return False
    return True


def main(number: int):
    largest_prime_factor = 1
    limit = number

    if number % 2 == 0:
        largest_prime_factor = 2
        limit = limit / largest_prime_factor

    i = 3
    while i <= limit:
        if i % 1000 == 0:
            print(i)
        if is_prime(i) and number % i == 0:
            limit = limit / i
            largest_prime_factor = i
        i += 2

    print(largest_prime_factor)


if __name__ == '__main__':
    main(600851475143)
