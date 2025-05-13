class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = Counter(target)
        for x in arr:
            if x not in counter:
                return False
            else:
                counter[x] -= 1
                if counter[x] < 0:
                    return False
        return True