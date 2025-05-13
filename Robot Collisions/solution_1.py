class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        aux = sorted([[positions[i],healths[i], directions[i], i] for i in range(len(positions))])
        for x in aux:
            if stack and stack[-1][2] == 'R' and x[2] == 'L':
                if stack[-1][1] == x[1]:
                    stack.pop()
                elif stack[-1][1] > x[1]:
                    stack[-1][1] -= 1
                else:
                    stack.pop()
                    x[1] -= 1
                    stack.append(x)
            else:
                stack.append(x)
        stack.sort(key=lambda x: x[3])
        return [x[1] for x in stack]