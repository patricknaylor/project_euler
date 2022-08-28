############################################
#
# Project Euler Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2+b^2=c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
############################################

# pythagorean triples come in a 2-parameter family; but 1000 is small enough that we can easily brute force this
# although this is not particularly efficient, it will certainly work

def find_triple():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000-a-b
            if a**2+b**2 == c**2:
                return [a, b, c], a*b*c


answer = find_triple()

print("The triple is {}, the product of these numbers is: {}.".format(answer[0], answer[1]))
