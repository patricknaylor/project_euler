###########################################
#
# Project Euler Problem 23
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n,
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis,
# even though it is known that the greatest number that cannot be
# expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
###########################################

bound = 28123


# this function "d" is the same as in Problem 22; define a function to calculate it.
# since 28123 isn't very large, this function doesn't need to be particularly clever
def sum_divisors(number):
    d = 0
    for k in range(1, number):
        if number % k == 0:
            d += k
    return d


# now, make a dictionary storing the values of this function
divisor_lib = {}
for i in range(1, bound):
    divisor_lib[i] = sum_divisors(i)

# make a list storing the abundant numbers
abundant = [num for num in divisor_lib.keys() if divisor_lib[num] > num]
print("Made a list of all abundant numbers less than {}.".format(bound))

# now make a list of numbers which -are- sums of abundant numbers
sum_of_abundant = []

for num1 in abundant:
    for num2 in abundant:
        if num1 + num2 < bound:
            sum_of_abundant.append(num1 + num2)

# then, convert this to a set to avoid duplication
sum_of_abundant_set = set(sum_of_abundant)

# to get the sum of numbers which -aren't- sums of abundant numbers;
# subtract the sum of the previous set from the sum of integers from 1 to (28123-1).
total = int(28122 * 28123 / 2) - sum(sum_of_abundant_set)
print("The sum of numbers not equal to a sum of two abundant numbers is {}.".format(total))
