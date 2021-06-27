from itertools import chain
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                num = min(matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j])
                if matrix[i][j]:
                    matrix[i][j] += num
        return sum(chain(*matrix))