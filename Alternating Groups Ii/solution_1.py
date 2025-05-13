class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        res = 0
        lcur = 1; prev_color = colors[0]

        for i in range(1, length + k - 1):
            index = i % length

            if colors[index] == prev_color:
                lcur = 1
                prev_color = colors[index]
                continue

            lcur += 1
            if lcur >= k:
                res += 1

            prev_color = colors[index]

        return res