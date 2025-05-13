class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def can_assign(k):
            available = workers[-k:]  # k strongest
            task_list = tasks[:k]     # k easiest
            used = [False] * k
            j = k - 1
            i = k - 1 
            pills_left = pills

            while j >= 0:
                if available[i] >= task_list[j]:
                    i -= 1
                    j -= 1
                elif pills_left > 0:
                    found = False
                    for p in range(i + 1):
                        if available[p] + strength >= task_list[j]:
                            available.pop(p)
                            i -= 1
                            pills_left -= 1
                            j -= 1
                            found = True
                            break
                    if not found:
                        return False
                else:
                    return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res