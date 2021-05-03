from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for left, right in zip(l, r):
            cur_arr = sorted(nums[left:right + 1])
            temp = cur_arr[1] - cur_arr[0]
            for i in range(len(cur_arr) - 1):
                if cur_arr[i + 1] - cur_arr[i] != temp:
                    answer.append(False)
                    break
            else:
                answer.append(True)
        return answer