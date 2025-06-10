class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {}

        def find(c):
            if c not in d:
                d[c] = c
            if d[c] != c:
                d[c] = find(d[c])
            return d[c]

        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2:
                return
            if p1 < p2:
                d[p2] = p1
            else:
                d[p1] = p2

        for a, b in zip(s1, s2):
            union(a, b)

        ans = ''
        for c in baseStr:
            ans += find(c)
        return ans
