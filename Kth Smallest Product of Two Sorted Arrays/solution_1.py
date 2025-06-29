class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        len_nums2 = len(nums2)
        def ceil_div(x, a):
            if a > 0:
                return (x + a - 1) // a
            else:
                return (x + a + 1) // a
        
        
        def count_le_pairs(mid):
            counter = 0
            for x in nums1:
                if x == 0:
                    if mid >= 0:
                        counter += len_nums2
                elif x > 0:
                    r = bisect_right(nums2, mid // x)
                    counter += r
                else:
                    threshold = ceil_div(mid, x)
                    l = bisect_left(nums2, threshold)
                    counter += len_nums2 - l
            return counter
        
        left, right = -10**11, 10**11
        while left < right:
            mid = (left+right) // 2
            if count_le_pairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
