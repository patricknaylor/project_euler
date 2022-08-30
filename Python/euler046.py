###########################################
#
# Project Euler Problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can be written
# as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#
###########################################


# as usual, we'll begin by getting a list of all the prime numbers up to a large bound
# the primes are stored a boolean list; true means that index is prime

def get_primes(bound):
    primes = [True for _ in range(bound)]
    primes[0], primes[1] = False, False

    p = 2

    while p * p < bound:

        # given a prime number p
        if primes[p]:

            # all multiples of p aren't prime!
            for n in range(p * p, bound, p):
                primes[n] = False

        # lastly, increment the number
        p += 1

    return primes


# we'll start with all the primes up to 10*
is_prime = get_primes(10**7)
primes_list = [p for p in range(10**7) if is_prime[p]]


# this function uses our primes list to check if a number satisfies the conjecture
def check_goldbach(num):

    # for each prime in our primes list
    for p in range(2, num - 1):

        if is_prime[p]:
            sqr = int((num - p) / 2)
            sqrt = sqr**0.5

            if int(sqrt)**2 == sqr:
                return True

    return False


# now, just search for a while! 
def find_counterexample():

    n = 9

    # search indefinitely
    while True:
        
        if n > 10**9:
            raise "too big"
        
        # if n is an odd composite number
        if not is_prime[n] and n % 2 != 0:

            if not check_goldbach(n):

                return n

        n += 2


print("The first counterexample to this conjecture is {}.".format(find_counterexample()))
