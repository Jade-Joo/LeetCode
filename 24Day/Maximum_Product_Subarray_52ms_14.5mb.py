class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])            
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans
        '''
        [2, 3, -2, 4]
        max_prod, min_prod, ans = 2, 2, 2
        nums[i], max_prod*nums[i], min_prod*nums[i] = 3, 6, 6
        
        max_prod, min_prod, ans = 6, 3, 6
        nums[i], max_prod*nums[i], min_prod*nums[i] = -2, -6, -12
        
        max_prod, min_prod, ans = -2, -12, 6
        nums[i], max_prod*nums[i], min_prod*nums[i] = 4, -8, -48
        
        max_prod, min_prod, ans = 4, -48, 6
        ans = 6
        '''        