############################################
#
#Project Euler Problem 24
#
#A permutation is an ordered arrangement of objects.
#For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
#The lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#
############################################


# I found this conceptually tricky. Given a 10 digit sequence, the following function computes
# the next (10 digit) number with respect to the lexicographic ordering.
# for convenience (and to save memory), we'll store the numbers as sequences, and modify them in place.

term = 1000000
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# the following function computes the next 'lexicographic' element. I had to play with some small examples to
# figure this out-- one can also find explicit algorithms onlien

def next_term(number):

    # first, find the first index in which the sequence is -not- in descending order
    for i in range(9)[::-1]:
        if number[i] < number[i+1]:
            index = i
            break

    # then, find the largest index which has a bigger value than the original one 
    for j in range(index + 1, 10)[::-1]:
        if number[j] > number[index]:
            swap = j
            break

    # now, swap these indices
    number[index], number[swap] = number[swap], number[index]

    # and reverse the rest of the sequence
    number[index + 1:] = number[index + 1:][::-1]


# this function just finds the n-th term and returns it as a string
def find_term(term):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1,term):
        next_term(number)
        
    # having just learned about "map," this is a nice way to convert back to an int.
    # map converts each element to a str; these are joined to the empty string
    return "".join(map(str,number))


print("The {}-th term is {}.".format(term,find_term(term)))

    
     

    
    
