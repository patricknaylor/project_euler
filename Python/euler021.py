###########################################
#
#Project Euler Problem 21
#
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#f d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.
###########################################

bound = 10000

#this bound is fairly small, so we can just compute the values for d in the worst way possible
def d_function(number):
    d = 0
    for i in range(1,number):
        if number%i == 0:
            d += i
    return d

#now, make a dictionary storing the values of this function
d_library = {}
for i in range(1,bound):
    d_library[i]=d_function(i)

#now, add the set of amicable numbers to a list
amicable_numbers = []
for number in d_library:
    d = d_library[number]
    if d in d_library.values() and d < bound and d > 0 and d_library[d] == number and d != number: #check that they satisfy all the requisite conditions
        amicable_numbers.append(d)

print("The amicable numbers under {} are {}; their sum is {}.".format(bound,amicable_numbers,sum(amicable_numbers)))
#The answer is 31626


        
