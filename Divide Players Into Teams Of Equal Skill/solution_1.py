class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        if sum(skill) != (skill[0] + skill[-1]) * (len(skill) // 2):
            return -1
        
        left = 0; right = len(skill) - 1
        chemistry = 0
        while left < right:
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        return chemistry