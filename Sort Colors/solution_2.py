class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def insertion_sort(my_list):
            for i in range(1, len(my_list)):
                j = i - 1
                while j >= 0 and my_list[j+1] < my_list[j]:
                    my_list[j+1], my_list[j] = my_list[j], my_list[j+1]
                    j -= 1
            return my_list
        
        insertion_sort(nums)
