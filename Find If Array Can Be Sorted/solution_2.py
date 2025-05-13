class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        set_bits = format(nums[0], '0b').count('1')
        seg_max = nums[0]; seg_min = nums[0]
        prev_seg_max = -1

        for i in range(1, len(nums)):
            if format(nums[i], '0b').count('1') == set_bits:
                seg_max = max(seg_max, nums[i])
                seg_min = min(seg_min, nums[i])
            else:
                if seg_min < prev_seg_max:
                    return False
                
                prev_seg_max = seg_max
                
                # start a news segment with this element
                seg_max = nums[i]; seg_min = nums[i]
                set_bits = format(nums[i], '0b').count('1')
        
        if seg_min < prev_seg_max:
            return False
        return True