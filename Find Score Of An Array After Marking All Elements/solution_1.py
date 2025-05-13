class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0; l = len(nums)
        order = [el[0] for el in sorted(list(enumerate(nums)), key=lambda x: x[1])]
        marked = set()
        for index in order:
            if index not in marked:
                score += nums[index]
                marked.add(index)
                if index - 1 >= 0:
                    marked.add(index-1)
                if index + 1 < l:
                    marked.add(index+1)
        return score