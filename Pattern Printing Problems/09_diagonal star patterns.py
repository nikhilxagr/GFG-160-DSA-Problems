# diagonal star patterns

# Time Complexity: O(N) where N is number of nodes in a given binary tree

# Auxiliary Space: O(N)For the given input, this program prints the following pattern. The input must be an odd number.
# Examples: 
 

# Input : 7
# Output :

#     *******
#     **   **
#     * * * *
#     *  *  *
#     * * * *
#     **   **
#     *******

def pattern(n) :
    
    #  for rows
    for i in range(0 , n) :

        # for columns
        for j in range(0 , n) :
            
            # Checking boundary conditions and main
            # diagonal and secondary diagonal conditions
            
            if (i == 0 or j == 0 or i == j  
               or i == n - 1 or j == n - 1 
               or i + j == n - 1) :
                
                print( "*", end="")
            else :
                print(" ",end="")
        
        print("")
    
n = 7
pattern(n)