class Solution(object):
    def threeSum(self, nums: list) -> list:
        nums.sort() #ascending
        N, result = len(nums), []

        #i = current index
        for i in range(N):
            #remove duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #num[i] = a = -(b + c) = target
            target = nums[i]*-1

            left, right = i+1, N-1
            while left < right:
                #find
                if nums[left]+nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                #bigger
                elif nums[left] + nums[right] < target:
                    left += 1
                #smaller
                else:
                    right -= 1
        return result

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    inst = Solution()
    res = inst.threeSum(nums)
    print(res)
