class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid_index = len(nums) // 2
        left = self.sortArray(nums[:mid_index])
        right = self.sortArray(nums[mid_index:])

        return merge(left, right)
    
    def merge(self, list1, list2):
        combined = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1
        if i == len(list1):
            combined.extend(list2[j:])
        else:
            combined.extend(list1[i:])
        return combined