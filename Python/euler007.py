####################################################
#
# Project Euler Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
#
####################################################

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


# then, make a list of the prime numbers
is_prime = get_primes(1000000)
primes_list = [p for p in range(1000000) if is_prime[p]]

index = 10001

print("The {}-th prime number is {}.".format(index, primes_list[index]))
