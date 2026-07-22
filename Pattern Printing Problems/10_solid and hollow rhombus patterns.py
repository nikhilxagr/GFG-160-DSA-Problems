# solid and hollow rhombus patterns


# For any given number n, print Hollow and solid Squares and Rhombus made with stars(*). 
# Examples: 
 

# Input : n = 4
# Output : 
# Solid Rhombus:
#    ****
#   ****
#  ****
# ****

# Hollow Rhombus:
#    ****
#   *  *
#  *  *
# ****


def solidRhombus(rows):
    
    for i in range (1,rows + 1):
        
        # Print  spaces
        
        for j in range (1,rows - i + 1):
            print (end=" ")
            
        # Print stars
        
        for j in range (1,rows + 1):
            print ("*",end="")
            
        # Move to the next line
        print()


def hollowRhombus(rows):
    
    for i in range (1, rows + 1):
        # Print spaces
        
        for j in range (1, rows - i + 1):
            print (end=" ")
            
        # Print stars
        
        if i == 1 or i == rows:
            for j in range (1, rows + 1):
                print ("*",end="")
                
        # stars for hollow rows
        
        else:
            for j in range (1,rows+1):
                if (j == 1 or j == rows):
                    print ("*",end="")
                else:
                    print (end=" ")
                    
        # Move to the next line/row
        print()

def printPattern(rows):
    
    print ("Solid Rhombus:")
    solidRhombus(rows)
    
    print("\nHollow Rhombus:")
    hollowRhombus(rows)

if __name__ == "__main__":
    
    rows = 5
    printPattern (rows)