class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        aux = []
        turn_point = -1

        for i in range(l-1, -1, -1):
            if nums[i] > nums[i-1]:
                aux.append(nums[i])
                turn_point = nums[i-1]
                nums[i-1], nums[i] = nums[i], nums[i-1]
                break
            else:
                aux.append(nums[i])
        if len(aux) == l:
            nums.sort()
            return None
        
        if len(aux) > 1:
            position = bisect_right(aux, turn_point)
            aux.insert(position, turn_point)
            nums[l-len(aux)] = aux.pop(position+1)
            m = len(aux)
            for i in range(m-1, -1, -1):
                nums[l-1 - (m-1) + i] = aux[i]