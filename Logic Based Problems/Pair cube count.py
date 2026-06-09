# Pair cube count
 
 
# Given a positive integer n, count all pairs of ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = n.

# Example :

# Input: n = 9 
# Output: 2
# Explanation: There are two solutions: (a=1, b=2) and (a=2, b=1).
# Input: n = 27
# Output: 1
# Explanation: Thereis only one solution: (a=3, b=0). 

# ALGORITHM:
 """Return number of pairs (a>=1, b>=0) with a^3 + b^3 == n.

    Simple and readable: compute integer cube-root bound, make a set
    of cubes, then check for each a whether the remainder is a cube.
    O(n^(1/3)) time and space.
    """





class Solution:
    def pairCubeCount(self, n):
       
        if n < 1:
            return 0

        # approximate integer cube root and adjust
        
        max_root = int(n ** (1/3))
        
        while (max_root + 1) ** 3 <= n:
            max_root += 1
        while max_root ** 3 > n:
            max_root -= 1

        cubes = {i ** 3 for i in range(max_root + 1)}

        count = 0
        for a in range(1, max_root + 1):
            if (n - a ** 3) in cubes:
                count += 1

        return count