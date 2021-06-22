from functools import reduce
from typing import List
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        n = 2 ** maximumBit
        res = reduce(lambda x, y : x ^ y, nums) #reduce(ixor, nums)
        while nums:
            answer.append(res ^ (n - 1))
            res ^= nums.pop()
        return answer