# Add two fractions


# You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).

# Input Format:
# The first line of input contains an integer T denoting the number of test cases . Then T test cases follow . Each test case contains four integers num1, den1, num2, den2 respectively .

# Output Format:
# For each test case, in a new line,  output will be the fraction in the form a/b where the fraction denotes the sum of the two given fractions in reduced form.

# Your Task:
# Since this is a function problem, you don't need to worry about the testcases. Your task is to complete the function addFraction  which adds the two fractions and prints the resulting fraction. The function takes four arguments num1, den1, num2, den2 where num1, num2 denotes the numerators of two fractions and den1, den2 denotes their denominators.

#Your task is to complete this function
#Your shouldn't return any thing it should print the required output

def addFraction(num1, den1, num2, den2):
    
    # code here
    
    from math import gcd
    
    numx = num1*den2 + num2*den1
    denx = den1*den2
    
    common = gcd(numx, denx)
    
    numx //= common
    denx //= common
    
    print(f"{numx}/{denx}")