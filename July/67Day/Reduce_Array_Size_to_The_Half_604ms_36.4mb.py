from collections import Counter
from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = sorted(Counter(arr).items(), key=lambda x: x[1])
        
        answer = 0
        while cnt:
            cur_cnt = cnt.pop()[1]
            n -= cur_cnt
            answer += 1
            if n <= len(arr)//2:
                break
                
        return answer