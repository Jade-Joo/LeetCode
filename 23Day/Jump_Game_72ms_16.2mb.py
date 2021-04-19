class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= n:
                n = i
                
        return not n