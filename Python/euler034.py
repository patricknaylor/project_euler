#######################################
#
# Project Euler Problem 34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of
# the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
#
#######################################

# we need an upper bound of numbers to check
# if a number has k digits, then its factorial sum is at most k*9! = 362880*k
# so, if it has 8 digits, then its factorial sum is at most 362880*8 = 2903040
# which is impossible!
# thus, we only need to check numbers with at most 7 digits, i.e. less than 10000000

big_bound = 10000000


def find_curious_numbers(bound):

    list_of_numbers = []
    
    # define the factorial function
    def factorial(n):
        product = 1
        for i in range(1, n+1):
            product *= i
        return product
            
    # we don't need to check 1 & 2
    for number in range(3, bound):

        digits = list(map(int, list(str(number))))
        factorial_digits = map(factorial, digits)
        factorial_sum = sum(factorial_digits)

        if number == factorial_sum:
            list_of_numbers.append(number)

    return list_of_numbers


curious_numbers = find_curious_numbers(big_bound)

print("The only curious numbers are: {}. Their sum is {}.".format(curious_numbers, sum(curious_numbers)))
