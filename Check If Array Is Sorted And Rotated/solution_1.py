class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        aux = nums * 2
        print(aux)
        for i in range(n):
            for j in range(i, i+n-1):
                if aux[j] > aux[j+1]:
                    break
            else:
                return True
        
        return False