###########################################
#
# Project Euler Problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
###########################################

# first, we need to find an upper bound where this certainly can't be possible
# if there are k digits, the largest sum possible is k*9**5 = 59049*k
# if there are 7 digits, the largest sum possible is 413343, which only has 6 digits.
# so, any such number has at most 6 digits, i.e. is less than 1000000

bound = 1000000
  
def find_special_numbers(bound):

    # we'll store the numbers we find in a list
    special_numbers = []
    
    # we don't count 0 or 1
    for number in range(2,bound):

        # now, get the sum of the 5-th powers of digits of each number
        # we convert the number into a list of digits using the map function
        digits = list(map(int,list(str(number))))

        # then, get the sum using another map and a lambda function
        sum_of_powers = sum(list(map(lambda x : x**5, digits)))

        # if we find one, add it to our list
        if sum_of_powers == number:
            special_numbers.append(number)

    return special_numbers


# find all these numbers, and print the result!
print("The sum of these special numbers is {}.".format(sum(find_special_numbers(bound))))
