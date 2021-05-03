from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        #52ms 15.4mb
        # n = len(nums)
        # cnt = 0
        # cur_idx = 0
        # for i in range(n):
        #     if nums[i]:
        #         nums[cur_idx] = nums[i]
        #         cur_idx += 1
        #     else:
        #         cnt += 1
        # for j in range(n - cnt, n):
        #     nums[j] = 0