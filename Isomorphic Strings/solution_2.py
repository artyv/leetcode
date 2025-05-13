class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        checked_letters = set()

        for i in range(len(s)):
            if s[i] not in checked_letters:
                print(f"{checked_letters=} {t=}")
                t = t[:i] + t[i:].replace(t[i], s[i])
                checked_letters.add(s[i])
        return s == t