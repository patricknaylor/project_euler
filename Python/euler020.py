############################################
#
# Project Euler Problem 20
#
# Find the sum of the digits in the number 100!
#
############################################

# python should be able to handle this!

big_num = 1
for i in range(1, 101):
    big_num *= i

sum_of_digits = sum([int(i) for i in str(big_num)])

print("The sum of the digits of 100! is {}.".format(sum_of_digits))
