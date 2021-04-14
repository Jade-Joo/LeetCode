class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start = -1
        cnt = 0
        for idx, n in enumerate(nums):
            if n == target:
                if start == -1:
                    start = idx
                cnt += 1
        return [start, start + cnt - 1]