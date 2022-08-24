###############################################
#
# Project Euler Problem 25
#
# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
#
###############################################

# store two terms, with their indices

current_term = [1, 2]
previous_term = [1, 1]

# this function will return the index of the first fibonacci number with that number of digits

def find_index(digits):

    found = False
    
    while found == False:
        
        next_term = current_term[0] + previous_term[0]
        next_index = current_term[1] + 1

        if len(str(next_term)) >= digits:
            found = True
            return next_index
        
        else:
            previous_term[0] = current_term[0]
            previous_term[1] = current_term[1]
            current_term[0] = next_term
            current_term[1] = next_index


print("The index of the first term of the Fibonacci sequence with 1000 digits is {}.".format(find_index(1000)))
    
# The answer is 4782    

