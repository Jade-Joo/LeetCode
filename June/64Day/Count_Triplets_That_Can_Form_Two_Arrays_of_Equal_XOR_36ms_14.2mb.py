class Solution:
    def countTriplets(self, A: List[int]) -> int:
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(A):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res

'''
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        A.insert(0, 0)
        n = len(A)
        for i in range(n - 1):
            A[i + 1] ^= A[i]
        
        # A = [0, 2, 1, 0, 6, 1]
        
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if A[i] == A[j]:
                    res += j - i - 1
        return res
'''