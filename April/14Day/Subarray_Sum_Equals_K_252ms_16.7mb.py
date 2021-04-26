from collections import defaultdict
class Solution:
    def __init__(self):
        self.answer = 0
        
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp = defaultdict(int)
        temp[0] = 1
        
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in temp:
                self.answer += temp[cur_sum - k]
            temp[cur_sum] += 1
        return self.answer