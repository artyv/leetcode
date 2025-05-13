class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def can_assign(k):
            task_deque = deque(tasks[:k])
            available = workers[-k:]
            pill_count = pills
            i = k - 1  # index of strongest available

            for j in reversed(range(k)):
                if available[j] >= task_deque[-1]:
                    task_deque.pop()
                else:
                    if pill_count == 0:
                        return False
                    if available[0] + strength < task_deque[0]:
                        return False
                    for x in range(k):
                        if available[x] + strength >= task_deque[0]:
                            available.pop(x)
                            break
                    task_deque.popleft()
                    pill_count -= 1
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