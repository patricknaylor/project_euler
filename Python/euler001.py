################################################
#
# Project Euler Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
################################################

# we can do this by simply counting these numbers (the bound is small, so we won't worry about speed).
def sum_integers(bound):

    count = 0
    for i in range(bound):
        if i % 3 == 0 or i % 5 == 0:
            count += i
            
    return count


print("The sum of these numbers is {}.".format(sum_integers(1000)))
