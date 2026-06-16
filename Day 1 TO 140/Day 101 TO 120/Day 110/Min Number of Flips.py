# Min Number of Flips

# Given a binary string s of length n. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.

# Examples:

# Input: s = "001"
# Output: 1
# Explanation: We can flip the 0th bit to 1 to have "101".
# Input: s = "0001010111" 
# Output: 2
# Explanation: We can flip the 1st and 8th bit. After this we have "0101010101"

class Solution:
    def minFlips(self, s):
        
        count1 = 0
        count2 = 0

        for i in range(len(s)):
            
            if i % 2 == 0 and s[i] == '1':
                count1 += 1
            elif i % 2 == 1 and s[i] == '0':
                count1 += 1
            elif i % 2 == 0 and s[i] == '0':
                count2 += 1
            elif i % 2 == 1 and s[i] == '1':
                count2 += 1

        return min(count1, count2)