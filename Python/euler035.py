#######################################
#
# Project Euler Problem 35
#
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
#
#######################################


# first, we'll get a list of all primes up to one million using a sieve
# store the primes as a boolean list; true means that index is prime

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


# next, decide if each prime in our list is circular!
# in short: get a list of all primes below a million, and check if each is circular
# a smart way would remove circulants as they are created, but this seems to work just fine

def get_circular_primes(bound):
    prime_list = get_primes(bound)
    primes = [i for i in range(bound) if prime_list[i]]
    circular_primes = []

    def circulate(num):
        return int(str(num)[-1] + str(num)[:-1])

    # for each prime number
    for p in primes:

        is_circular = True
        circle_p = p

        # check if it's circular! 
        for k in range(len(str(p))):
            circle_p = circulate(circle_p)

            # if some circulant isn't prime, break the loop and move on
            if circle_p not in primes:
                is_circular = False
                break

        # otherwise, add it to the list of circular primes
        if is_circular:
            circular_primes.append(p)

    return circular_primes


print("There are {} circular primes below 1 million.".format(len(get_circular_primes(1000000))))
