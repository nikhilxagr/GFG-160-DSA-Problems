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
        sum_value = int(a, 2) + int(b, 2)
        return bin(sum_value)[2:]


obj = Solution()   
print(obj.addBinary("1101", "111"))  # Output: "10100"