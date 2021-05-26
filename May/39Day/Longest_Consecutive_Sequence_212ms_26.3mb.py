from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        answer = 0
        prev_num = None
        cnt = 0
        for n in nums:
            if prev_num == None:
                prev_num = n
                cnt += 1
                continue
            if prev_num + 1 == n:
                prev_num = n
                cnt += 1
            else:
                answer = max(answer, cnt)
                prev_num = n
                cnt = 1
            print(n, cnt)
        return max(answer, cnt)

'''
[Brute Force]
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
'''

'''
[Sorting]
class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)
'''

'''
[HashSet and Intelligent Sequence Building]
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
'''