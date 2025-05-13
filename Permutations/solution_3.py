class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def perm_recursive(curr):
            if(len(curr) == len(nums)):
                permutations.append(curr)

            for num in nums:
                if(not num in curr):
                    perm_recursive(curr.copy() + [num])


        perm_recursive([])
        return permutations

