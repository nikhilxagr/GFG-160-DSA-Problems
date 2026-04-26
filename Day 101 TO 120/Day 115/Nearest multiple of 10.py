    # Nearest multiple of 10

    # A string s is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from s, choose the smallest element among them.

    # Examples:

    # Input: s = "29" 
    # Output: 30
    # Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 
    # Input: s = "15"
    # Output: 10
    # Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.
    

class Solution:
    def roundToNearest(self, s):
        last = int(s[-1])

        # Round down (including tie case 5)
        if last <= 5:
            if len(s) == 1:
                return "0"
            return s[:-1] + "0"

        # Round up
        num = str(int(s[:-1] or "0") + 1)
        return num + "0"