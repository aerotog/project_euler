
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


def irrational_fraction_array():
    numbers = []
    i = 1
    while len(numbers) < 1_000_000:
        for c in str(i):
            numbers.append(int(c))
        i += 1
    return numbers


def main():
    nums = irrational_fraction_array()
    result = 1

    for i in range(0, 6):
        target = 10 ** i
        nth_digit = nums[target - 1]
        result *= nth_digit

    print(result)


if __name__ == '__main__':
    main()
