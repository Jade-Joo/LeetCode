from typing import List
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        leaf = 1
        q = 1
        while leaf < label:
            leaf += 2 ** q
            q += 1
        else:
            q -= 1
        
        matrix = []
        for i in reversed(range(q + 1)):
            if i % 2 == 0:
                leaf -= 2 ** i
                tmp = [leaf + j for j in range(1, 2 ** i + 1)]
            else:
                tmp = []
                for _ in range(2 ** i):               
                    tmp.append(leaf)
                    leaf -= 1
            matrix.append(tmp)
        
        answer = []
        cur_idx = matrix[0].index(label)
        for k in range(q):
            answer.append(matrix[k][cur_idx])
            cur_idx  = cur_idx // 2
        answer += [1]
        return answer[::-1]
        
'''
class Solution:
    def pathInZigZagTree(self, label):
        res = [] # O(log n) space
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count*2: # O(log n) time
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0: # O(log n) time
            res.append(label)
            level_max = 2**(level) - 1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label)/2)
            level -= 1
        return res[::-1] # O(n) time
'''