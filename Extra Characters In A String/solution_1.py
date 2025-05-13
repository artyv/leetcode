class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        l = len(s)
        my_set = set(dictionary)

        dp = [0] * (l+1)

        for start in range(l-1, -1, -1):
            dp[start] = 1 + dp[start+1]
            for end in range(start, l):
                cur = s[start: end+1]
                if cur in my_set:
                    dp[start] = min(dp[start], dp[end+1])

        return dp[0]