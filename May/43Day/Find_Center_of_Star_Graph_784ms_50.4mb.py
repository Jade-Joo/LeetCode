from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        tmp = set()
        for i, j in edges:
            if i in tmp:
                return i
            if j in tmp:
                return j
            tmp.add(j)
            tmp.add(i)
        