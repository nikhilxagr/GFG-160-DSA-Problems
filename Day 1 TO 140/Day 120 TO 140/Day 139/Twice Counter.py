# Twice Counter

# Given a list of words. Count the number of words that appear exactly twice in the list.

# Examples:

# Input: list[] = [Geeks, For, Geeks]
# Output: 1
# Explanation: 'Geeks' is the only word that appears twice. 
# Input: list[] = [Tom, Jerry, Thomas, Tom, Jerry, Courage, Tom, Courage]
# Output: 2
# Explanation: 'Jerry' and 'Courage' are the only words that appears twice

class Solution:
    def countWords(self, List):
        
        count = {}
        
        for word in List:
            
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        twice_counter = 0
        
        for word, freq in count.items():
            if freq == 2:
                twice_counter += 1

        return twice_counter