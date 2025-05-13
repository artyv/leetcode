class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if Counter(start) != Counter(target) or start.replace('_', '') != target.replace('_', ''):
            return False
        
        l_start_pos = []; r_start_pos = []
        l_target_pos = []; r_target_pos = []
        
        for i, c in enumerate(start):
            if c == 'L':
                l_start_pos.append(i)
            elif c == 'R':
                r_start_pos.append(i)
        
        for i, c in enumerate(target):
            if c == 'L':
                l_target_pos.append(i)
            elif c == 'R':
                r_target_pos.append(i)
        
        for i in range(len(l_start_pos)):
            if l_target_pos[i] > l_start_pos[i]:
                return False
        
        for i in range(len(r_start_pos)):
            if r_target_pos[i] < r_start_pos[i]:
                return False
        
        return True

            