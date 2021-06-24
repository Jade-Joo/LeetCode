class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        def helper(N, i, j):
            if (N, i, j) in memo: return memo[(N, i, j)]
            if N == 0: return 0
            ans = 0
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n:
                    ans += helper(N - 1, i + x, j + y)
                else:
                    ans += 1
            memo[(N, i, j)] = ans
            return ans
        return helper(maxMove, startRow, startColumn) % (10**9 + 7)

'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        nxt = [[0] * n for _ in range(m)]
        nxt[startRow][startColumn] = 1

        ans = 0
        for time in range(maxMove):
            cur = nxt
            nxt = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD

        return ans
'''

'''
import numpy as np
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        paths = np.zeros((m, n), dtype=object)
        paths[i][j] = 1
        out = 0
        for _ in range(N):
            prev = paths
            paths = prev * 0
            paths[1:] += prev[:-1]
            paths[:-1] += prev[1:]
            paths[:,1:] += prev[:,:-1]
            paths[:,:-1] += prev[:,1:]
            out += 4 * prev.sum() - paths.sum()
        return out % (10**9 + 7)
'''