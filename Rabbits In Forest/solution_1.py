class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = 0
        for x in set(answers):
            counter += x + 1
        if answers.count(0):
            counter += answers.count(0) - 1
        return counter