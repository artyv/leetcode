class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {x:True for x in arr}

        for x in arr:
            if 2*x in d:
                return True
        return False