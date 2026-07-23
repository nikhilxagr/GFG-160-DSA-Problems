# Butterfly Pattern

# Given an integer N, print a butterfly star pattern with 2N − 1 rows. The number of stars increases from 1 to N in the upper half and then decreases from N − 1 to 1 in the lower half, forming a symmetric butterfly shape.

# Examples:

# Input: 3
# Output: 
# *      *
# **  **
# *****
# **  **
# *      *

# Input: 5
# Output: 
# *              *
# **          **
# ***      ***
# ****  ****
# *********
# ****  ****
# ***      ***
# **          **
# *              *

n = int(input())

# Upper half
for i in range(1, n + 1):
    if i == n:
        print('*' * (2 * n - 1))
    else:
        print('*' * i + ' ' * (2 * (n - i) - 1) + '*' * i)

# Lower half
for i in range(n - 1, 0, -1):
    print('*' * i + ' ' * (2 * (n - i) - 1) + '*' * i)