class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat

'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #row, col
        m, n = len(mat), len(mat[0])
        start_list = [(0,0)] + [(i, 0) for i in range(1, m - 1)] + [(0, i) for i in range(1, n - 1)]
        for r, c in start_list:
            arr = []
            val = []
            while r != m and c != n:
                arr.append((r, c))
                val.append(mat[r][c])
                r += 1
                c += 1
            val.sort()
            
            for l, v in zip(arr, val):
                mat[l[0]][l[1]] = v
        return mat
                
'''