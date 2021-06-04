class Solution:
    def minOperations(self, n: int) -> int:
        return ((n * n) // 2) // 2

'''
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [i * 2 + 1 for i in range(n)]
        answer = 0
        target = sum(arr) // len(arr)
        for i in range(n//2):
            answer += (target - arr[i])
        return answer
'''