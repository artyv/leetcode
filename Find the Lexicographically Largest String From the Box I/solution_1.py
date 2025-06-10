class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        largest_letter = max(word)
        max_length = len(word) - (numFriends-1)
        
        largest_string = ''
        for i,c in enumerate(word):
            if c == largest_letter:
                largest_string = max(largest_string, word[i:i+max_length]) # no need to care about i+max_length > len(word)
        return largest_string
