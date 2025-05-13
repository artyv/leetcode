class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if all(x % 2 == 1 for x in (arr[i], arr[i+1], arr[i+2])):
                return True
        return False