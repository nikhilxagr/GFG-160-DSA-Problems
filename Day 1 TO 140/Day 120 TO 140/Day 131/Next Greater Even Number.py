# Next Greater Even Number

# Given a positive integer x. The task is to find the smallest even number e such that e > x and all digits in x and e are the same.
# Note: If no possible number exists then return -1.

# Example 1:

# Input: x = 34722641
# Output: 34724126
# Explanation: Next greater number with same digits as in input is 34724126.
# Input: x = 111
# Output: -1
# Explanation: You can't rearrange the digits to get an answer.


class Solution:
    def getNextEven(self, x: str) -> int:

        num = list(x)
        n = len(num)

        while True:

            # Find breakpoint
            i = n - 2
            while i >= 0 and num[i] >= num[i + 1]:
                i -= 1

            if i < 0:
                return -1

            # Find next greater element
            j = n - 1
            while num[j] <= num[i]:
                j -= 1

            # Swap
            num[i], num[j] = num[j], num[i]

            # Reverse right part
            num[i + 1:] = reversed(num[i + 1:])

            # Check even
            if int(num[-1]) % 2 == 0:
                return int(''.join(num))