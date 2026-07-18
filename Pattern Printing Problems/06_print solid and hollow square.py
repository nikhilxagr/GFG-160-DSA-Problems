# print solid and hollow square patterns

# For any given number n, print Hollow and solid Squares and Rhombus made with stars(*). 
# Examples: 
 

# Input : n = 4
# Output : 

# Solid Square:
# ****
# ****
# ****
# ****

# Hollow Square:
# ****
# *  *
# *  *
# ****

class solution:
    
    def solid_square(self, n):
        for i in range(n):
            print('*' * n)

    def hollow_square(self, n):
        for i in range(n):
            
            if i == 0 or i == n - 1:
                print('*' * n)
            else:
                print('*' + ' ' * (n - 2) + '*')
            
# Approach - Print a solid square of size n x n, then print a hollow square of the same size.