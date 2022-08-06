#########################################
#Project Euler Problem 10
#
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#########################################


#first, get a list of all primes less than the specified bound using a sieve
#there might be a more clever way to implement the sieve without storing the whole list
#but this will certainly work

def get_primes(bound): 
    integers = [i for i in range(bound)]

    i = 2 #start at the first prime
    while i*i < bound: #only have to remove elements up to sqrt(bound)
        for j in range(i+1,bound):
            if j%i == 0:
                integers[j] = 0 
        i += 1
    primes = [item for item in integers if item != 0 and item !=1]
    return primes


bound = 2000000
sum  = sum(get_primes(bound))

print("The sum of the primes less than {} is {}.".format(bound, sum))

#The answer is 142913828922
