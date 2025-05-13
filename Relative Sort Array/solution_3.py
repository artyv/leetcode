class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        map_arr2 = {x:i for i,x in enumerate(arr2)}
        shift_constant = len(arr1) # can be whatever greater than len(arr1)

        def my_sort(x):
            if x in map_arr2:
                return map_arr2[x]
            else:
                return x + shift_constant
        
        return sorted(arr1, key=my_sort)