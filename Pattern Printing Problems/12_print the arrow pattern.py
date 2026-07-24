# print the arrow pattern
# Given the value of n, print the arrow pattern.
# Examples : 
 

# Input : n = 5
# Output : 

#  *
#   **
#    ***
#     ****
#      *****
#     ****
#    ***
#   **
#  *

# Input : n = 7
# Output : 

#  *
#   **
#    ***
#     ****
#      *****
#       ******
#        *******
#       ******
#      *****
#     ****
#    ***
#   **
#  *


import math

def print_arrow(n):

    # for upper part
    
    for i in range(1,n):
 
        # for space 
        for j in range(0,i):
            print(" ",end="")
 
        # for printing stars in upper
        for k in range(0,i):
            print("*",end="")
        
        print()
    
    for i in range(0,n):
 
       # for space
        for j in range (0,n-i):
            print(" ",end="")
        
        # for printing stars in lower part
        for k in range (0,n-i):
            print("*",end="")
        
        print()

n = 6
print_arrow(n)