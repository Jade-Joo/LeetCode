class Solution:
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j] # A[j] 가 0이면 -1이 됨
            if K < 0:
                K += 1 - A[i] #A[i] 가 0이면 +1
                i += 1
        return j - i + 1