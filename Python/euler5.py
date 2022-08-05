############################################
#Project Euler Problem 5
#
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
############################################


#one could certainly use import math and python's lcm function.
#alternatively, this is easy to compute directly;
#lcm(1*2*...*10)=2*2*2*5*3*7*3=2520
#to get lcm(1*2*...*20), we only need a few more prime factors; 
#lcm(1*2*...*20)=(2*2*2*5*3*7*3)*(11*13*2*17*19)=232792560


#we can instead make this work by computing the gcd via the euclidean algorithm
#if a=bq+r then gcd(a,b)=gcd(b,r); and gcd(a,0)=a.

#this will only return positive integers
def gcd(num1,num2):

    a=max(abs(num1),abs(num2))
    b=min(abs(num1),abs(num2)) #easier if a>=b
    r=a%b

    if r == 0: return b
    
    while r != 0:
        a = b
        b = r
        r=a%b
    return b

def lcm(a,b):
    return int(a*b/gcd(a,b))

#now iterate to get the lcm of 1 ... 20
lowest_multiple = 1
for i in range(1,21):
    lowest_multiple = lcm(lowest_multiple,i)

print("The LCM of the numbers 1,...,20 is {}.".format(lowest_multiple))


#In either case, the answer is 232792560
