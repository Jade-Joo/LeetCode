class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        idx = 0
        temp = [-1]
        answer = []
        while idx < len(intervals):
            cur_interval = intervals[idx]
            cur_start, cur_end = cur_interval
            
            if cur_end <= temp[-1]:
                idx += 1
                continue
            
            nxt_end = cur_end
            for start, end in intervals[idx + 1:]:
                if nxt_end >= start and end > nxt_end:
                    nxt_end = end
            temp.append(nxt_end)
            answer.append([cur_start, nxt_end])
            idx += 1
        return answer