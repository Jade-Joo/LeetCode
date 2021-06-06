from typing import List
from collections import deque
# BFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        end = max([max(i) for i in graph if len(i)])
        m, n = len(graph), len(graph[0])
        q = deque([[0]])
        while q:
            cur_path = q.popleft()
            cur_node = cur_path[-1]
            nxt_nodes = graph[cur_node]
            if cur_path[-1] == end:
                answer.append(cur_path)
            else:
                for nxt_node in nxt_nodes:
                    q.append(cur_path + [nxt_node])
        return answer

'''
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1: res.append(path)
            else:
                for i in graph[cur]: dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
'''