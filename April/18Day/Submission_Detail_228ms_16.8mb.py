from itertools import chain
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if max(chain(*matrix)) == '0':
            return 0
        row, col = len(matrix), len(matrix[0])
        answer = 1
        for i in range(row - 1):
            for j in range(col  - 1):
                if matrix[i][j] > '0' and matrix[i + 1][j] > '0' and matrix[i][j + 1] > '0' and matrix[i + 1][j + 1] > '0': #1
                    matrix[i + 1][j + 1] = str(min(int(matrix[i][j]), int(matrix[i][j + 1]), int(matrix[i + 1][j])) + 1)
                    answer = max(answer, int(matrix[i + 1][j + 1]))
        return answer ** 2
                