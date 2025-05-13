class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return output