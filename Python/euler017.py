##################################################
#
# Project Euler Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
#
##################################################

# we will make a dictionary to store a number as a key, and the text version of that number as a value
# the first 20 or so values need to be hard coded, as do the multiples of 10 and 100
# everything else we won't add manually

# there is probably a more generic way to do this,

def get_names(bound):
    names = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
             10: "ten"}
    names.update(
        {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
         18: "eighteen", 19: "nineteen"})
    names.update(
        {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"})
    names.update({100: "one hundred"})
    names.update({1000: "one thousand"})

    if bound > 1001:
        print("Error: need to describe more numbers.")
        return []

    for number in range(1, bound):  # go through the list of names
        if number not in names:  # don't overwrite anything
            ones = number % 10
            tens = int((number - ones) / 10) % 10
            hundreds = int(number / 100)

            if hundreds == 0:  # there are some mutually exclusive cases here for naming conventions
                name = names[10 * tens] + " " + names.get(ones, "")

            elif hundreds != 0 and number % 100 == 0:
                name = names[hundreds] + " hundred"

            elif hundreds != 0:
                name = names[hundreds] + " hundred and " + names.get(10 * tens + ones)
            else:
                raise "Something went wrong!"

            names.update({number: name})
    return names


# now, all we have to do is add everything up
names_list = get_names(1001)
total = 0
for n in names_list:
    total += sum([len(name) for name in names_list[n].split()])

print("{} characters were used.".format(total))
