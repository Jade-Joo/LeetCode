from collections import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_top = [0] * col
        max_left = [0] * row
        
        for i in range(row):
            max_left[i] = max(grid[i])
            for j in range(col):
                max_top[j] = max(max_top[j], grid[i][j])
        
        answer = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] < min(max_left[i], max_top[j]):
                    answer += min(max_left[i], max_top[j]) - grid[i][j]
        return answer