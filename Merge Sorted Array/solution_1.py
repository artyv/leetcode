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

        i, j = m-1, n-1
        for k in range(m+n-1, -1, -1):
            if j == -1 or i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                if i >= 0:
                    i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        return self


