class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {arr[i]:i for i in range(len(arr))}

        for i, x in enumerate(arr):
            if 2*x in d and i != d[2*x]:
                return True
        return False