class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(list1, list2):
            combined = []
            i, j = 0, 0
            l1, l2 = len(list1), len(list2)
            while i < l1 and j < l2:
                if list1[i] <= list2[j]:
                    combined.append(list1[i])
                    i += 1
                else:
                    combined.append(list2[j])
                    j += 1
            if i == l1:
                combined.extend(list2[j:])
            else:
                combined.extend(list1[i:])

            return combined    
        
        def merge_sort(my_list):
            if len(my_list) == 1:
                return my_list
            mid_index = len(my_list) // 2
            left = merge_sort(my_list[:mid_index])
            right = merge_sort(my_list[mid_index:])

            return merge(left, right)
        
        nums[:] = merge_sort(nums)