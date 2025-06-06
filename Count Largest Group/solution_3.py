class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        d = {}
        for x in range(1, n+1):
            #s = sum_digits(x)
            s = sum(map(int, str(x)))
            d[s] = d.get(s, 0) + 1
        
        largest_size = max(d.values())
        return sum(1 for x in d.values() if x == largest_size)