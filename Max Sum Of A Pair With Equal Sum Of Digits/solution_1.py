class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def digits_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        xmax = -1
        d = {}
        for x in nums:
            s_temp = digits_sum(x)
            if s_temp in d:
                d[s_temp].append(x)
            else:
                d[s_temp] = [x]
        
        for values in d.values():
            if len(values) < 2:
                continue
            values.sort()
            xmax = max(xmax, values[-1] + values[-2])
        
        return xmax
