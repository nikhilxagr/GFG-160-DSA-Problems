# Generate IP Addresses

# Given a string s containing only digits, your task is to restore it by returning all possible valid IP address combinations. You can return your answer in any order.

# A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255(inclusive).

# Note: The numbers cannot be 0 prefixed unless they are 0. For example, 1.1.2.11 and 0.11.21.1 are valid IP addresses while 01.1.2.11 and 00.11.21.1 are not.

# Examples:

# Input: s = “255678166”
# Output: [“25.56.78.166”, “255.6.78.166”, “255.67.8.166”, “255.67.81.66”]
# Explanation: These are the only valid possible IP addresses.

# Input: s = “25505011535”
# Output: []
# Explanation: We cannot generate a valid IP address with this string.



class Solution:
    def generateIp(self, s):
        ans = []
        for i in range(1, 4):
            
            for j in range(i + 1, i + 4):
                for k in range(j + 1, j + 4):
                    if k < len(s):
                        a = s[:i]
                        b = s[i:j]
                        c = s[j:k]
                        d = s[k:]
                        
                        if (int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255 and
                            (a == "0" or a[0] != "0") and
                            (b == "0" or b[0] != "0") and
                            (c == "0" or c[0] != "0") and
                            (d == "0" or d[0] != "0")):
                            ans.append(f"{a}.{b}.{c}.{d}")
      
        return ans
    
    
# s = "255678166"
# ans = []
# for i in range(1, 4):
#     for j in range(i + 1, i + 4):
#         for k in range(j + 1, j + 4):
#             if k < len(s):
#                 a = s[:i]
#                 b = s[i:j]
#                 c = s[j:k]
#                 d = s[k:]
                
#                 if (int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255 and
#                     (a == "0" or a[0] != "0") and
#                     (b == "0" or b[0] != "0") and
#                     (c == "0" or c[0] != "0") and
#                     (d == "0" or d[0] != "0")):
#                     ans.append(f"{a}.{b}.{c}.{d}")
# print(ans)