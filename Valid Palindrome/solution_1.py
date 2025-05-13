class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified_s = ''.join(c for c in s.lower() if c.isalnum())
        
        left, right = 0, len(modified_s) - 1

        while left < right:
            if modified_s[left] != modified_s[right]:
                return False
            left += 1
            right -= 1
        return True
