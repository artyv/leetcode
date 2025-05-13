class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        d = {}
        for word in words2:
            c2 = Counter(word)
            for k,v in c2.items():
                if d.get(k, 0) == 0:
                    d[k] = v
                else:
                    d[k] = max(d[k], v)

        for word in words1:
            c1 = Counter(word)
            for k,v in d.items():
                if d[k] > c1.get(k, 0):
                    break
            else:
                res.append(word)
        
        return res