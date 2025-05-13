class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        counter = Counter(digits)
        for x in range(100, 1000, 2):
            cnt = Counter(map(int, list(str(x))))
            for d, v in cnt.items():
                if d not in counter or v > counter[d]:
                    break
            else:
                res.append(x)

        return res 