from math import comb
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4)

'''
[Top down]
def countVowelStrings(self, n):
    seen = {}
    def dp(n, k):
        if k == 1 or n == 1: return k
        if (n, k) in seen:
            return seen[n, k]
        seen[n, k] = sum(dp(n - 1, k) for k in xrange(1, k + 1))
        return seen[n, k]
    return dp(n, 5)

[Bottom up]
def countVowelStrings(self, n):
    dp = [[1] * 6] + [[0] * 6 for i in xrange(n)]
    for i in xrange(1, n + 1):
        for k in xrange(1, 6):
            dp[i][k] = dp[i][k - 1] + dp[i - 1][k]
    return dp[n][5]

[accumulate]
from itertools import accumulate
def countVowelStrings(self, n: int) -> int:
    dp = [1] * 5
    for i in range(n):
        dp = accumulate(dp)
    return list(dp)[-1]
'''