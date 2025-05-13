class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            cur_char = nums[i][i]
            ans.append('1' if cur_char == '0' else '0')
        
        return ''.join(ans)
