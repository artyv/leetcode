class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        counter = Counter(digits)
        for x in range(100, 1000, 2):
            x1, x2, x3 = (x // 100), (x // 10) % 10, x % 10
            if any(x not in counter for x in (x1, x2, x3)):
                continue
            counter[x1] -= 1
            counter[x2] -= 1
            counter[x3] -= 1

            if counter[x1] >= 0 and counter[x2] >= 0 and counter[x3] >= 0:
                res.append(x)
            
            counter[x1] += 1
            counter[x2] += 1
            counter[x3] += 1

        return res 