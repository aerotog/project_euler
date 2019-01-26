
# It is well known that if the square root of a natural number is not an integer, then it is irrational.
# The decimal expansion of such square roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356237309504880...,
# and the digital sum of the first one hundred decimal digits is 475.
#
# For the first one hundred natural numbers,
# find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.


def get_sqrt(target: int) -> str:
    # Based on algo "Digit-by-digit calculation" from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    x = get_x(target, "0")
    f = function(x, "0")
    remainder = target - f
    p = str(x)

    while len(p) < 100:
        c = remainder * 100
        x = get_x(c, p)
        f = function(x, p)
        remainder = c - f
        if remainder == 0:
            break
        p += str(x)

    return p


def function(x: int, p) -> int:
    return x * (20 * int(p) + x)


def get_x(c: int, p: str) -> int:
    for i in range(9, -1, -1):
        if function(i, p) <= c:
            return i


def main():
    sum = 0

    for i in range(2, 100):
        sqrt = get_sqrt(i)
        if not len(sqrt) < 100:
            print(i)
            print(sqrt)
            for c in str(sqrt):
                sum += int(c)
    print(sum)


if __name__ == '__main__':
    main()
