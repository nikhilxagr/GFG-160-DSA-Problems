# co-prime or not

# Two numbers A and B are said to be Co-Prime or mutually prime if the Greatest Common Divisor of them is 1. You have been given two numbers A and B, find if they are Co-prime or not.
# Examples : 
 

# Input : 2 3
# Output : Co-Prime

# Input : 4 8
# Output : Not Co-Prime

def __gcd(a, b):

    # Everything divides 0 
    if (a == 0 or b == 0): return 0
    
    # base case
    if (a == b): return a
    
    if (a > b): 
        return __gcd(a - b, b)
            
    return __gcd(a, b - a)

def coprime(a, b):
    
    if ( __gcd(a, b) == 1):
        print("Co-Prime")
    else:
        print("Not Co-Prime")     


a = 5; b = 6
coprime(a, b) 

a = 8; b = 16
coprime(a, b)