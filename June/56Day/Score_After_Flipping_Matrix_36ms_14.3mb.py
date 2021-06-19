class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = (1 << N - 1) * M # 열의 길이만큼 shift
        for j in range(1, N):
            cur = sum(grid[i][j] == grid[i][0] for i in range(M)) # 0열과 각 열이 같을 때 개수
            res += max(cur, M - cur) * (1 << N - 1 - j) # 현재 열 만큼 shift하여 move가 되는 것들의 최대 개수만큼 곱함
        return res