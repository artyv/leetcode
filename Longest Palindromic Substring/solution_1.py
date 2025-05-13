class Solution:
    def longestPalindrome(self, s: str) -> str:
        smax = s[0]

        palindromes = []
        for i in range(len(s)):
            palindromes.extend(self.findPalindrome(s, i-1, i+1))
            palindromes.extend(self.findPalindrome(s, i, i+1))
        return sorted(palindromes, key=len)[-1]

    def findPalindrome(self, s: str, j: int, k: int) -> List[str]:
        palindromes = []
        while j >= 0 and k < len(s):
            if s[j] != s[k]:
                break
            palindromes += [s[j:k+1]]
            j -= 1; k += 1
        return palindromes
