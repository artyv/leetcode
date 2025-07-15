class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set('aeiouAEIOU')
        if len(word) >= 3 and word.isalnum() and \
            any(c in vowels for c in word) and \
            any(c.isalpha() and c not in vowels for c in word):
            return True
        return False
