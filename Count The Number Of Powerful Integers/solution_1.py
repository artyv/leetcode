class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        start_str = str(start - 1)
        finish_str = str(finish)
        
        return self.calculate(finish_str, suffix, limit) - self.calculate(start_str, suffix, limit)

    def calculate(self, x: str, suffix: str, limit: int) -> int:
        if len(x) < len(suffix):
            return 0
        
        if len(x) == len(suffix):
            return 1 if x >= suffix else 0

        prefix = x[:len(x) - len(suffix)]
        suffix_part = x[len(x) - len(suffix):]
        count = 0

        for i in range(len(prefix)):
            if int(prefix[i]) > limit:
                count += (limit + 1) ** (len(prefix) - i)
                return count
            
            count += int(prefix[i]) * (limit + 1) ** (len(prefix) - 1 - i)


        if suffix_part >= suffix:
            count += 1

        return count
