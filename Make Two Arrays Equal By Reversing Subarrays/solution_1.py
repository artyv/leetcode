class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = Counter(target)
        for x in arr:
            if x not in counter:
                return False
        return True