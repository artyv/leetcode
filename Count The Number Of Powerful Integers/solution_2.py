class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def is_valid(x_str, limit, finish):
            if len(x_str) > len(str(finish)):
                return False
            if any(int(d) > limit for d in x_str):
                return False

            x_int = int(x_str)
            return start <= int(x_str) <= finish

        results = []

        def dfs(curr_str):
            if len(curr_str) > len(str(finish)):
                return        
            
            if is_valid(curr_str, limit, finish):
                results.append(int(curr_str))

            for d in range(limit + 1):
                dfs(str(d) + curr_str)

        dfs(s)
        print(results)

        return len(set(results))