class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0; right = len(skill) - 1
        chemistry = 0
        reference_value = skill[left] + skill[right]
        while left < right:
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            if skill[left] + skill[right] != reference_value:
                return -1
        return chemistry