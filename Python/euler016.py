#########################################
#
# Project Euler Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#
#########################################

# this one is quick in python!

def sum_of_digits(number):
    return sum([int(i) for i in str(number)])


print("The sum of the digits is {}.".format(sum_of_digits(2**1000)))
