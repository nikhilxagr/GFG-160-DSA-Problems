# Palindrome Sentence

# Given a single string s, the task is to check if it is a palindrome sentence or not.
# A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the same backward as forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters (including spaces and punctuation).

# Examples:

# Input: s = "Too hot to hoot"
# Output: true
# Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "toohottohoot" which is a palindrome.
# Input: s = "Abc 012..## 10cbA"
# Output: true
# Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters to lowercase, string s will become "abc01210cba" which is a palindrome.
# Input: s = "ABC $. def01ASDF"
# Output: false
# Explanation: The processed string becomes "abcdef01asdf", which is not a palindrome.


class Solution:
    def isPalinSent(self, s):
        # code here
        s = s.lower().strip()
        s = s.replace(" ", "")
        ans = []
        
        for i in s:
            if i.isalnum():
                ans.append(i)
        ans = ''.join(ans)

        if ans == ans[::-1]:
            return True
        else:
            return False