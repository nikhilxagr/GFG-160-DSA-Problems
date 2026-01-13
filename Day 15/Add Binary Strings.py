# Add Binary Strings

# Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
# Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

# Example -

"""
Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100

Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
  
  """
  
class Solution:
    def addBinary(self, a, b):
        # Start from the last characters
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = []

        # Loop while there are digits left or a carry
        while i >= 0 or j >= 0 or carry == 1:

            # Get digit from a
            if i >= 0:
                x = int(a[i])
            else:
                x = 0

            # Get digit from b
            if j >= 0:
                y = int(b[j])
            else:
                y = 0

            # Add digits and carry
            total = x + y + carry

            # Binary digit result
            digit = total % 2
            result.append(str(digit))

            # Update carry
            carry = total // 2

            # Move pointers
            i -= 1
            j -= 1

        # Reverse result and join into string
        result.reverse()
        return "".join(result)
 