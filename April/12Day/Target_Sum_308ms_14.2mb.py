from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        cnt = Counter({0 : 1})
        for cur_n in nums:
            tmp = Counter()
            for i in cnt:
                tmp[i + cur_n] += cnt[i]
                tmp[i - cur_n] += cnt[i]
            cnt = tmp
        return cnt[S]