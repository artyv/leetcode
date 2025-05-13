class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        aux = [0] * n
        aux[-1] = questions[-1][0]

        for i in range(n-2, -1, -1):
            j = i + (questions[i][1] + 1)
            extra = 0 if j >= n else aux[j]
            aux[i] = max(questions[i][0] + extra, aux[i+1])
        
        return max(aux)