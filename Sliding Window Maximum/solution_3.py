class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        window = deque()
        a = []

        for i, n in enumerate(nums):
            # remove indices outside of our window
            while window and window[0] < i-k+1:
                window.popleft()
            
            # remove everything that is less than current element, so max element index is always window[0]
            while window and nums[window[-1]] < n:
                window.pop()
        
            window.append(i)
    
            if i >= k-1:
                a += [nums[window[0]]]
        
        return a
