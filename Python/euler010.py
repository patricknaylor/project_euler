#########################################
#
# Project Euler Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
#########################################


# first, get a list of all primes less than the specified bound using a sieve

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


is_prime = get_primes(2000000)
sum_primes = sum([p for p in range(2000000) if is_prime[p]])

print("The sum of the primes less than {} is {}.".format(2000000, sum_primes))
