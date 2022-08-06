##########################################
#
#Project Euler Problem 18
#By starting at the top of the triangle below and moving to adjacent numbers on the row below,
#the maximum total from top to bottom is 23.
#
#3
#7 4
#2 4 6
#8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:
#75
#95 64
#17 47 82
#18 35 87 10
#20 04 82 47 65
#19 01 23 75 03 34
#88 02 77 73 07 63 67
#99 65 04 28 06 16 70 92
#41 41 26 56 83 40 80 70 33
#41 48 72 33 47 32 37 16 94 29
#53 71 44 65 25 43 91 52 97 51 14
#70 11 33 28 77 73 17 78 39 68 17 57
#91 71 52 38 17 14 91 43 58 50 27 29 48
#63 66 04 68 89 53 67 30 73 16 69 87 40 31
#04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
#However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
##########################################



#we don't want to brute force this problem -- that will wind up being a lot of additions.
#instead, note that the paths are ordered! They're in bijection with binary numbers less than 2^15, which are definitely ordered.
#what we'll try to do is work our way through this space of paths, keeping track of the sum as we go.
#hopefully, this will be smart enough for Problem 67 (update: it isn't)

#first, we'll get the triangle using some list comprehension
input_triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

small_triangle = '''3
7 4
2 4 6
8 5 9 3'''

triangle = [list(map(int, row.split())) for row in input_triangle.split("\n")] 
        
#now we have a matrix form of the triangle
#we will view paths as a binary number with 15 digits, where 000000000000000 means the leftmost path, and 011111111111111 is the rightmost path (they always start with 0)

#this takes a path and returns the actual matrix coordinates
def path_to_coor(path):
    coor = [[0,0]]
    for i in range(1,len(path)):
        coor.append([i,coor[i-1][1]+int(path[i])])
    return coor


#this function will check all the paths and return the largest path, together with its sum
def largest_path(triangle):
    height = len(triangle)
    path = path_to_coor('0'*height) #this is the first path
    path_sum = sum([triangle[path[i][0]][path[i][1]] for i in range(height)]) #this is the first path sum

    max_path_sum = path_sum #initialize the starting maxima
    max_path = path
    for i in range(2**(height-1)):
        new_binary_i = str(bin(i))[2:] #binary numbers come with the prefix 0b; we'll store these as strings to be able to get the indices easily; and add a prefix and drop the first two characters.
        new_path_binary = "0"*(height-len(new_binary_i))+new_binary_i
        new_path = path_to_coor(new_path_binary)
        #new_path_sum = sum([triangle[new_path[j][0]][new_path[j][1]] for j in range(height)])

        new_path_sum = path_sum

        #the plan here: we want to keep track of the sum of a path, and then as we change paths, modify this sum only where the actual numbers have changed:
        for item in [i for i in range(height) if path[i][1] != new_path[i][1]]: #ie all the columns where the path differs
            new_path_sum += - triangle[item][path[item][1]] + triangle[item][new_path[item][1]]            

        #now, we have the new path sum.
        if new_path_sum > max_path_sum:
            max_path_sum = new_path_sum
            max_path = new_path

        #now, increment the variables and run again
        path = new_path
        path_sum = new_path_sum

    return max_path_sum, max_path

#output the answer! 

print("The sum of the largest path is {}.".format(largest_path(triangle)[0]))

#The answer is 1074
