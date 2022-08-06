##################################################
#Project Euler Problem 6
#
#The sum of the squares of the first ten natural numbers is 1^2+2^2+...+10^2 = 385
#The square of the sum of the first ten natural numbers is (1+2+...+10)^2 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
##################################################

#This should be easy enough to brute force; however, there is certainly a better way to do this using a little bit of algebra. 

number = 100

#this function just computes both numbers and subtracts them
def sq_of_sum_minus_sum_of_sq(number):
    
    sum_of_squares = 0
    square_of_sum = 0

    for i in range(number+1):
        sum_of_squares += i**2 

    square_of_sum = int((number*(number+1)/2)**2)
    return square_of_sum-sum_of_squares



print("The difference is {}.".format(sq_of_sum_minus_sum_of_sq(number)))

#The answer is 25164150.
