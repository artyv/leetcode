class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        a = list(map(int, s))
        while len(a) != 1 or a[0] != 1:
            if a[-1] % 2 == 0:
                a.pop(-1)
            else:
                a[-1] = 0
                for i in range(len(a)-2, -1, -1):
                    if a[i] == 1:
                        a[i] = 0
                    else:
                        a[i] = 1
                        break
                else:
                    a.insert(0, 1)
            steps += 1
        return steps