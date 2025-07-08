class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[0])
        len_events = len(events)
        start_days = [x[0] for x in events]
        end_i = -1

        @lru_cache
        def dp(i, remaining):
            if i == len_events or remaining == 0:
                return 0
            # skip
            res = dp(i+1, remaining)
            # take
            end_i = events[i][1]
            next_index = bisect_right(start_days, end_i)
            
            res = max(res, events[i][2] + dp(next_index, remaining - 1))
            return res
        
        return dp(0, k)
