class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)

        z1_count = nums1.count(0)
        z2_count = nums2.count(0)

        if z1_count == 0 and s1 < s2 + z2_count or z2_count == 0 and s2 < s1 + z1_count:
            return -1
        
        s1 += z1_count
        s2 += z2_count

        return max(s1, s2)
