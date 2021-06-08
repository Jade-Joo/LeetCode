from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3
        piles = piles[:-1]
        cnt = 0
        answer = 0
        for i in piles[::-2]:
            cnt +=1
            answer += i
            if cnt == n:
                break
        return answer