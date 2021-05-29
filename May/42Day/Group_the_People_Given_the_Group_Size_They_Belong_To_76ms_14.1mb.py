from typing import List 
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        for idx, val in enumerate(groupSizes):
            dic[val].append(idx)
        
        answer = []
        for k in dic.keys():
            for i in range(0, len(dic[k]), k):
                answer.append(dic[k][i:i + k])
 
        return answer