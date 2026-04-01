# Remove consonants from a string

# Given a string S, remove all consonants and print the modified string that contains vowels only.

# Example 1:

# Input
# S = "abEkipo"
# Output
# aEio
# Explanation : a, E, i, o are only vowels in the string.
# Example 2:

# Input
# S = "rrty"
# Output
# No Vowel
# Explanation: There are no vowels.

# Your Task: You don't need to read input or print anything. Your task is to complete the function removeConsonants() which takes a string S as input and returns the modified string that contains vowels only. If there are no vowels, return "No Vowel".



class Solution:
    def removeConsonants(self, s):
        vowels = "aeiouAEIOU"
        result = ""

        for char in s:
            if char in vowels:
                result += char

        return result if result else "No Vowel"