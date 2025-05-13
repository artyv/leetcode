class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        output = []
        for k in counter1.keys() & counter2.keys():
            output.extend([k]*min(counter1[k], counter2[k]))
        return output