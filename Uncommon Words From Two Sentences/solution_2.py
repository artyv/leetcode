class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst1 = s1.split()
        lst2 = s2.split()

        counter1 = Counter(lst1)
        counter2 = Counter(lst2)

        res = []

        for k, v in counter1.items():
            if v != 1:
                continue
            if counter2.get(k, 0) == 0:
                res.append(k)
        
        for k, v in counter2.items():
            if v != 1:
                continue
            if counter1.get(k, 0) == 0:
                res.append(k)
        return res