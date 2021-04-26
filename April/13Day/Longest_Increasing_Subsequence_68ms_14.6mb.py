from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            left, right = 0, size
            left = bisect_left(tails, n, lo=left, hi=right)
            tails[left] = n
            size = max(left + 1, size)
        return size