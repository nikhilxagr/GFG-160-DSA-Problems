# Closest Strings

# Given a list of words, S followed by two specific words, word1 and word2, the task is to find the minimum distance between the indices of these two words in the list.

# Note: word1 and word2 are both in the list, and there can be multiple occurrences of words in the list.

# Example :

# Input:S = { "the", "quick", "brown", "fox", "quick"}
# word1 = "the"
# word2 = "fox"
# Output: 3
# Explanation: Minimum distance between the words "the" and "fox" is 3

# Input:S = {"geeks", "for", "geeks", "contribute", "practice"}
# word1 = "geeks"
# word2 = "practice"
# Output: 2
# Explanation: Minimum distance between the words "geeks" and "practice" is 2


class Solution:
	def shortestDistance(self, s, word1, word2):
     
		min_dist = float('inf')
		index1 = -1
		index2 = -1

		for i in range(len(s)):
      
			if s[i] == word1:
				index1 = i
			if s[i] == word2:
				index2 = i

			if index1 != -1 and index2 != -1:
				min_dist = min(min_dist, abs(index1 - index2))

		return min_dist