class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        l = len(arr)
        chunks = 0
        prefix_sum = 0
        sorted_prefix_sum = 0

        for i in range(l):
            prefix_sum += arr[i]
            sorted_prefix_sum += i

            if prefix_sum == sorted_prefix_sum:
                chunks += 1

        return chunks