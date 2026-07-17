# Print the Diamond Shape
# Given a number n, print a diamond-shaped star pattern with 2n rows, where the number of stars first increases and then decreases to form the diamond.

n = int(input())
# code here

space = n - 1

# Upper half of the diamond

for i in range(0, n):
    # Print leading spaces
    
    for j in range(0, space):
        print(" ", end="")
    
    # Print stars
    
    for j in range(0, i + 1):
        print("* ", end="")
        
    print()
    space -= 1
    
space = 0
# Lower half of the diamond
for i in range(n, 0, -1):
    
    # Print  spaces
    for j in range(0, space):
        print(" ", end="")
    
    # Print stars
    
    for j in range(0, i):
        print("* ", end="")
        
    print()
    space += 1
    
# Approach :
    
# we first print the upper half of the diamond by printing leading spaces followed by stars.
# Then we print the lower half of the diamond in a similar manner, but in reverse order.
# The number of leading spaces decreases as we move down the upper half and increases as we move down the lower half.
    