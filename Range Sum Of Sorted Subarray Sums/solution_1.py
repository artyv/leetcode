class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        aux = []
        
        for i, x in enumerate(nums):
            aux.append(x)
            for j in range(i*(i-1)//2, i*(i+1)//2):
                aux.append(x + aux[j])
        
        aux.sort()
        return sum(aux[left-1:right])