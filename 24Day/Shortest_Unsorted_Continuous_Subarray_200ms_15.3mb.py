class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        
        check = []
        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                check.append(i)
        
        if len(check) > 1:
            return check[-1] - check[0] + 1
        else:
            return 0