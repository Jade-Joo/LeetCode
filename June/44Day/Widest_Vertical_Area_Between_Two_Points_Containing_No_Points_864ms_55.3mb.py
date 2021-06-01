class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        for x, y in points:
            arr.append(x)
        arr.sort()
        
        answer = 0
        for i in range(len(arr) - 1):
            answer = max(answer, arr[i + 1] - arr[i])
        return answer