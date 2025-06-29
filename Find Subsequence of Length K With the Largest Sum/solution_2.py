class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        top_k = heapq.nlargest(k, indexed_nums, key=lambda x: x[0])
        top_k_sorted = sorted(top_k, key=lambda x: x[1])

        return [val for val, _ in top_k_sorted]
