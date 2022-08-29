########################################
#
# Project Euler Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
#
########################################


# some math helps us out a lot here! This is a standard counting question.
# re label things so that we start at the origin, and head out towards the point (20,20).
# the number of paths from (i,j) to the origin is the sum of the paths from (i+1,j) and (i,j+1)
# moreover, there's only one path from a point of the form (i,20) or (20,i).
# in other words, the number of paths is a pascal triangle!
# the number of paths from (i,j) to the origin is just i choose i+j

# thus the answer is 20 choose 40;
from math import comb

print("There are {} such paths.".format(comb(40, 20)))
