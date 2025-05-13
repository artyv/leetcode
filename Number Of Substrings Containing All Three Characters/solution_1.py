class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = 0
        left = 0
        letters = {}
        length = len(s)

        for right in range(length):
            letters[s[right]] = letters.get(s[right], 0) + 1

            while len(letters) == 3:
                counter += length - right
                letters[s[left]] -= 1
                if letters[s[left]] == 0:
                    del letters[s[left]]
                left += 1

        return counter