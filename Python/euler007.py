####################################################
#Project Euler Problem 7
#
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
####################################################

#there are probably a few clever things we can do here,
#however, 10001 is small enough that brute force is still probably the quickest to code


#check if a number is prime-- in a brute force way
def is_prime(number):
    
    if number == 2 or number == 3 or number == 5: return True #make sure 2,3,5 do return true;
    if number%2 == 0 or number%3 == 0 or number%5 == 0: #then we can always rule out divisibility by 2,3,5 to speed things up
        return False
    
    for i in range(2,int(number**0.5)+1): #if it isn't divisible by 2,3 or 5, check the remaining odd numbers
        if number%i==0:
            return False
    return True

#find the bound-th prime number using the previous function
def find_prime(bound):
    prime_counter = 0
    num = 2

    while prime_counter != bound:
        if is_prime(num) == True:
            prime_counter += 1
        num += 1
        
    return num - 1

#set the bound = 10001, print the result
bound = 10001
print("The {}-th prime number is {}.".format(bound, find_prime(bound)))

#answer is 104743
