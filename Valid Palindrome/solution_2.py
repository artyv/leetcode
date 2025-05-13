class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
        return s == s[::-1]