##########################################
#
# Project Euler Problem 47
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?
#
##########################################

# as usual, we'll get a list of all prime numbers below a given bound; we'll start with 10**7
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


# we'll start with all the primes up to 10**7; we can add more if need be
is_prime = get_primes(10 ** 7)
primes_list = [p for p in range(10 ** 7) if is_prime[p]]


# this function returns a list of the prime factors of n (in increasing order)
def factors(n):
    factor_list = []
    k = n

    while k > 1:

        if is_prime[k]:
            factor_list.append(k)
            return factor_list
        else:
            for p in primes_list:
                if k % p == 0:
                    factor_list.append(p)
                    k = int(k / p)
                    break


# this function finds the first of k consecutive integers with k distinct prime factors
def find_cons_primes(k):
    i = 2
    found = False

    while True:

        for j in range(i, i + k):

            if len(set(factors(j))) != k:
                i += 1
                found = False
                break

        if found:
            return i

        found = True


print("The first number in a sequence of {} consecutive integers, each with {} distinct prime factors is: {}.".format(
    4, 4, find_cons_primes(4)))
