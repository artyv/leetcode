class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0; l = len(arr)
        while i < l-2:
            if arr[i] % 2 == 1:
                if arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                    return True
            i += 1
        return False