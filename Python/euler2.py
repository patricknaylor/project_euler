########################################################
#Project Euler Problem 2

#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
########################################################


#the upper bound isn't really that large, so we can just brute force this.
#if it were larger, we could use some tricks: only every third term will be even; there are closed form expressions for these terms, etc.

def sum_even(bound):
    
    total = 0

    term = 1
    next_term = term

    while next_term <= bound: #check that the term isn't about the bound yet
        if next_term%2 ==0:   # add to the total if it's even
            total += next_term
        next_term += term
        term = next_term - term #compute the next pair of terms in the sequence

    return total
    
    
print(sum_even(4000000))

#answer is 4613732
