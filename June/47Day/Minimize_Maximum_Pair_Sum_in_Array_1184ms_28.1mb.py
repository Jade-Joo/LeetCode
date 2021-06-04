class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        arr = sorted(nums)
        left, right = 0, len(nums) - 1
        answer = 0
        while left < right:
            answer = max(answer, arr[left] + arr[right])
            left += 1
            right -= 1
        return answer