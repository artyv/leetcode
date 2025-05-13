class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_s = ''.join(c for c in s.lower() if c.isalnum())
        return modified_s == modified_s[::-1]
