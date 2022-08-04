######################################################
#Project Euler Problem 3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
######################################################

#we could probably do this quickly with various packages, but I'm going to try to make each problem self contained

#brute force is probably not a solution
#we should probably make a list of all prime numbers using the sieve of Eratosthenes

big_number = 600851475143


#will return a list of all prime numbers less than bound
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

#check if a number is prime. In any case, return a list [T/F, factor, number/factor] to give us a factorization when it's not.
def is_prime(number): 

    if number in prime_list:
        return [True, number, 1]
    else:
        for prime in prime_list:
            if number%prime == 0:
                return [False, prime, int(number/prime)]

    
sqrt_big_number = int(big_number**0.5)
prime_list = get_primes(sqrt_big_number) #get a list of all possible factors of our large number. Perhaps this is unecessary, but if y
print("Found all primes up to {}.".format(sqrt_big_number))


#now, we'll completely factorize our number
#start with a list of factors

#this will take a list of factors, and return a prime decomposition of that list (in increasing order)
def factorize(factor_list):
    factor_list = [big_number]

    for item in factor_list:

        check = is_prime(item)
        
        if check[0] == False:
            factor_list.remove(item)
            factor_list.append(check[1])
            factor_list.append(check[2])
            
    return factor_list

print("The factors of {} are {}.".format(big_number,factorize(big_number)))

#The answer is 6857
#This computes way more prime numbers than necessary in this case, but in principle they might have been necessary.
#A better strategy might be to try smaller factors first, and only add to the prime_list as neccessary



