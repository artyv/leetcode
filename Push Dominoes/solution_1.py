class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        force = 0
        # left to right
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        
        res = []
        for f in forces:
            if f > 0:
                res.append('R')
            elif f < 0:
                res.append('L')
            else:
                res.append('.')
        return ''.join(res)