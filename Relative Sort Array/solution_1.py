class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cur_position = 0
        arr1.sort()
        #map_arr2 = {x:i for i,x in enumerate(arr2)}
        for x in arr2:
            for i in range(len(arr1)):
                if arr1[i] == x:
                    arr1[i], arr1[cur_position] = arr1[cur_position], arr1[i]
                    cur_position += 1
        return arr1