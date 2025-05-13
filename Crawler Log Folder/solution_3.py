class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0
        for x in logs:
            if x == '../':
                if counter > 0:
                    counter -= 1
            elif x == './':
                continue
            else:
                counter += 1
        return counter
            