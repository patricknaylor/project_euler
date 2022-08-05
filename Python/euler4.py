###########################################
#Project Euler Problem 4
#
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
###########################################


#1000 isn't so large, so this can be solved by brute force

def find_palindrome(bound):
    largest = 0

    for i in range(1000):
        for j in range(1000):
            if i*j > largest:
                if str(i*j)[::-1] == str(i*j): #iterate over all pairs of integers; using a useful trick in python to reverse a string
                    largest = i*j

    return largest

print("The largest such palindrome is {}.".format(find_palindrome(1000)))

#The answer is 906609
