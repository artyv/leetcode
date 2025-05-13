class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        prev = ''
        output = ''
        queue = deque(sorted(s, reverse=True))
        counter = 0
        while queue:
            if queue[0] != prev:
                counter = 0
                prev = queue[0]
            
            if counter < repeatLimit:
                output += queue.popleft()
            else:
                for i in range(len(queue)):
                    if queue[i] != prev:
                        output += queue[i]
                        del queue[i]
                        counter = -1
                        break
                else:
                    return output
            counter += 1
        return output