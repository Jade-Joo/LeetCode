from typing import List
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            x, y, r = query
            cnt = 0
            for point in points:
                pt_x, pt_y = point
                if (pt_x - x) ** 2 + (pt_y - y) ** 2 <= r ** 2:
                    cnt += 1
            answer.append(cnt)
        return answer