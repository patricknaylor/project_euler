#########################################
#
#Project Euler Problem 14
#
#The following iterative sequence is defined for the set of positive integers:
#
#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)
#
#It can be seen that the sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#NOTE: Once the chain starts the terms are allowed to go above one million.
#Which starting number, under one million, produces the longest chain?
#########################################


#We definitely don't want to just compute the length of the sequence for each number.
#instead, we'll record each integer with it's distance from 1, and use this to save computations

bound = 1000000

#this will be our main object; the second coordinate will record the distance from 1 but we'll set these to -1 for now.
collatz = [[i,-1] for i in range(0,bound+1)]

#this function just computes the next term in a sequence
def next_term(n):
    output = 0
    if n%2 == 0:
        output = int(n/2)
    else:
        output = 3*n+1
    return output


#this function attempts to use the collatz list to find the length of a sequence
def collatz_length(number):
    
    if number == 1: 
        collatz[1][1]=1
        return 1
    
    if number < bound and collatz[number][1] != -1: #for numbers less than our bound, re-use previous computation
        return collatz[number][1]
    
    else:
        length = collatz_length(next_term(number))+1 #otherwise, just do it directly

        if number < bound:
            collatz[number][1]=length
            
        return length


def compute_collatz(bound):
    
    for i in range(1,bound+1):
        collatz_length(i)

    num = 1
    max = 0
    for i in range(1,bound+1):
        if collatz[i][1] > max:
            num = i
            max = collatz[i][1]

    return collatz[num]

answer = compute_collatz(bound)
print("The number with the longest Collatz sequence is {}, with {} elements.".format(answer[0],answer[1]))

#Tnswer is 837799; with 525 steps.

    
