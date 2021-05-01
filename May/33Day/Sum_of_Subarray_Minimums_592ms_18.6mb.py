from typing import List
class Solution:
    """
    For example, if A = [10, 3, 4, 5, _3_, 2, 3, 10] and we would like to know #(j = 4) [the count of the second 3, which     is marked], we would find i = 1 and k = 5.

    From there, the actual count is #(j) = (j - i + 1) * (k - j + 1), as there are j - i + 1 choices i, i+1, ..., j for       the left index of the subarray, and k - j + 1 choices j, j+1, ..., k for the right index of the subarray.
    """
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        
        #right-most minimum
        stack = []
        prev = [None] * n
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            else:
                prev[i] = -1
            stack.append(i)
        print(prev)
        #left-most minimum
        stack = []
        next_ = [None] * n
        for j in range(n - 1, -1, -1):
            while stack and arr[j] < arr[stack[-1]]:
                stack.pop()
            if stack:
                next_[j] = stack[-1]
            else:
                next_[j] = n
            stack.append(j)
        print(next_)
        return sum([(i - prev[i]) * (next_[i] - i) * arr[i] for i in range(n)]) % mod