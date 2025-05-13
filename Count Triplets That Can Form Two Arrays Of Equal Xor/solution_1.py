class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Looking for sub-arrays of length >= 2 and xor = 0
        # If I have one sub-array of length l with xor = 0 then permutations give l-1 variants of picking j
        counter = 0
        left = 0; right = 1
        for left in range(len(arr)-1):
            xor = arr[left]
            for right in range(left+1, len(arr)):
                xor ^= arr[right]
                if xor == 0:
                    counter += right - left
        return counter