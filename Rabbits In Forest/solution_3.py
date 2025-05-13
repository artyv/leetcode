class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = 0
        for x in set(answers):
            cnt = answers.count(x)
            batches = cnt // (x + 1)
            if batches >= 1:
                counter += batches * (x + 1)
                cnt %= x + 1
            if cnt:
                counter += x + 1
            
        return counter