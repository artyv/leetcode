class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return None
        elif m == 0:
            nums1[:] = nums2
            return None
        i = 0; j = 0
        while i < n + m and j < n:
            if nums1[i] <= nums2[j] and nums1[i] != 0:
                i += 1
            else:
                nums1.pop(-1)
                nums1.insert(i, nums2[j])
                i += 1
                j += 1