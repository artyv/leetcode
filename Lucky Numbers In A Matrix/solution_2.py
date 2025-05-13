class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = [min(x) for x in matrix]
        maxs = [0]*len(matrix[0])
        output = []

        for row in matrix:
            mins.append(min(row))
            for j in range(len(row)):
                maxs[j] = max(maxs[j], row[j])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == mins[i] and matrix[i][j] == maxs[j]:
                    output.append(matrix[i][j])
        return output
