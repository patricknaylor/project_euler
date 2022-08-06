############################################
#
#Project Euler Problem 22
#
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?
############################################

#This should be relatively easy in python.

#open the file; save it to a string for now
with open("p022_names.txt") as f:
    names_string = f.read()

#clean up this data a bit 
names_split = names_string.split(",")
names = [name.strip('"') for name in names_split]

#sort the list; make a new list with scoring data
names.sort()

#I'm sure there's a better way to score words, but this will work
def score(word):
    points = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22,"W":23, "X":24, "Y":25, "Z":26}
    total = 0
    for letter in word:
        total += points[letter.upper()] #just in case they aren't all uppercase
    return total

#all that's left is to compute this big number
big_total = 0
for index in range(len(names)):
    big_total += (index+1)*(score(names[index]))

print("The total score of these names is {}.".format(big_total))

#The answer is 871198282


    
    
        
