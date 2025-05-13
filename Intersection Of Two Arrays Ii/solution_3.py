class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                output.append(x)
        return output
