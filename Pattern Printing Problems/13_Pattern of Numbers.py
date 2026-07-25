# Pattern of Numbers

# The idea of pattern based programs is to understand the concept of nesting of for loops and how and where to place the alphabets / numbers / stars to make the desired pattern.
# Write to program to print the pattern of numbers in the following manner using for loop 
 

#     1
#    232
#   34543
#  4567654
# 567898765

# In almost all types of pattern programs, two things that you must take care: 
 

# No. of lines
# If the pattern is increasing or decreasing per line?

n = 5
num = 1
gap = n - 1
for j in range(1, n + 1) :
    num = j
    for i in range(1, gap + 1) :
        print(" ", end="")
    gap = gap - 1
        
    for i in range(1, j + 1) :
        print(num, end="")
        num = num + 1
    
    num = num - 2
    for i in range(1, j) :
        print(num, end="")
        num = num - 1
    
    print()