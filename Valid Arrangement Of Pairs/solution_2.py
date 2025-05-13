class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        def check(x, y):
            start[x] -= 1
            if start[x] == 0:
                del start[x]
            end[y] -= 1
            if end[y] == 0:
                del end[y]
        
        start = Counter([x[0] for x in pairs])
        end = Counter([x[1] for x in pairs])

        res = []
        l = len(pairs)

        while len(res) < l:
            for x,y in pairs:
                if end.get(x, 0) == 0:
                    check(x, y)
                    res.append([x,y])
                    pairs.remove([x,y])
                    break
            else:
                for x,y in pairs:
                    if start.get(y, 0) != 0:
                        check(x,y)
                        res.append([x,y])
                        pairs.remove([x,y])
                        break
        return res
