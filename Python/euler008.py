#########################################################
#Project Euler Problem 8
#
#The four adjacent digits in the 1000-digit number below that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
#########################################################


#here is the 1000 digit number, stored as a string
big_number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'


#input a string and ouput the product of the digits; empty string gets assigned 1
def prod(string):
    product = 1
    for i in string:
        product = product * int(i)
    return product       


#just check each substring in a brute force way
#Probably a better way to do this-- only really need to know the difference in the ends of a substring to compare products
def greatest_prod(bignum, increment):
    product = 0
    index = 0
    max_index = 0
    
    for index in range(len(bignum)-increment-1):
        new_product = prod(bignum[index:index+increment])
        if new_product > product:
            product = new_product
            max_index = index
        index += 1
        
    return product, max_index

increment = 13
greatest_product, index = greatest_prod(big_number, increment)

print("The greatest product of {} adjacent digits is {}; the digits are {}.".format(increment, greatest_product, big_number[index:index+increment]))

#The answer is 23514624000, corresponding to the substring 30420752963450
