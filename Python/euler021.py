###########################################
#
# Project Euler Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
#
###########################################

# this bound is fairly small, so we can just compute the values for d in the worst way possible
def d_function(number):
    d = 0
    for k in range(1, number):
        if number % k == 0:
            d += k
    return d


def find_amicable_numbers(bound):

    # now, make a dictionary storing the values of this function
    d_library = {}
    for i in range(1, bound):
        d_library[i] = d_function(i)

    # now, add the set of amicable numbers to a list
    amicable_numbers = []
    for number in d_library:
        d = d_library[number]
        # check that they satisfy all the requisite conditions
        if d in d_library.values() and bound > d > 0 and d_library[d] == number and d != number:
            amicable_numbers.append(d)

    return amicable_numbers


amicable_numbers_list = find_amicable_numbers(10000)

print("The amicable numbers under {} are {}; their sum is {}.".format(
    10000, amicable_numbers_list, sum(amicable_numbers_list)))
