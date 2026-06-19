# # Digital Root

# You are given a number n. You need to find the digital root of n. Digital Root of a number is the recursive sum of its digits until we get a single digit number.

# Examples :

# Input: n = 1
# Output:  1
# Explanation: Digital root of 1 is 1
# Input: n = 99999
# Output: 9
# Explanation: Sum of digits of 99999 is 45 which is not a single digit number, hence sum of digit of 45 is 9 which is a single digit number.

class Solution:
    def digitalRoot(self, n: int) -> int:
        
    # If given number is zero its
    # digit sum will be zero only
        if n == 0:
            return 0

    # If result of modulo operation is
    # zero then, the digit sum is 9
        if n % 9 == 0:
            return 9

        return n % 9