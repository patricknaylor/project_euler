#########################################
#
# Project Euler Problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# It can be seen that the sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# NOTE: Once the chain starts the terms are allowed to go above one million.
# Which starting number, under one million, produces the longest chain?
#
#########################################

# we definitely don't want to just compute the length of the sequence for each number.
# instead, we'll record each integer with its distance from 1, and use this to save computations

# this will be our main object; the second coordinate will record the distance from 1, initialized at -1
collatz = [[i, -1] for i in range(1000000+1)]


def next_term(n):

    if n % 2 == 0:
        output = int(n/2)
    else:
        output = 3 * n + 1

    return output


# this function attempts to use the collatz list to find the length of a sequence
def collatz_length(number):
    
    if number == 1: 
        collatz[1][1] = 1
        return 1

    # for numbers less than our bound, re-use previous computation if possible
    if number < len(collatz) and collatz[number][1] != -1:
        return collatz[number][1]

    # otherwise, do it directly
    else:
        length = collatz_length(next_term(number)) + 1

        # record the computation for the future
        if number < len(collatz):
            collatz[number][1] = length
            
        return length


# this function computes the collatz number of all integers less than bound, and returns the one with the longest length
def compute_collatz(bound):
    
    for i in range(1, bound + 1):
        collatz_length(i)

    num = 1
    longest = 0

    for i in range(1, bound+1):
        if collatz[i][1] > longest:
            num = i
            longest = collatz[i][1]

    return collatz[num]


answer = compute_collatz(1000000)
print("The number with the longest Collatz sequence is {}, with {} elements.".format(answer[0], answer[1]))
