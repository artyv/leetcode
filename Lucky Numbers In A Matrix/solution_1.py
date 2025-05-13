class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        output = []

        columns = list(zip(*matrix))
        for row in matrix:
            min_row = min(row)
            if max(columns[row.index(min_row)]) == min_row:
                output.append(min_row)

        return output
