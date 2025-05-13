class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:  
        start = Counter([x[0] for x in pairs])
        end = Counter([x[1] for x in pairs])

        def check(x, y):
            start[x] -= 1
            if start[x] == 0:
                del start[x]
            end[y] -= 1
            if end[y] == 0:
                del end[y]

        res = []
        l = len(pairs)
        last_end = -1

        for x,y in pairs:
            if end.get(x, 0) == 0:
                check(x, y)
                res.append([x,y])
                pairs.remove([x,y])
                last_end = y
                break

        while pairs:
            for x,y in pairs:
                if (x == last_end or last_end == -1) and (start.get(y, 0) != 0 or len(pairs) == 1):
                    check(x,y)
                    res.append([x,y])
                    pairs.remove([x,y])
                    last_end = y
                    break
        return res
