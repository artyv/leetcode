class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def is_symmetric(x):
            x_str = str(x)
            l = len(x_str)
            if l % 2 == 1:
                return False
            mid = l // 2
            return sum(int(c) for c in x_str[:mid]) == sum(int(c) for c in x_str[mid:])
        
        counter = 0

        for x in range(low, high+1):
            if is_symmetric(x):
                counter += 1
        
        return counter