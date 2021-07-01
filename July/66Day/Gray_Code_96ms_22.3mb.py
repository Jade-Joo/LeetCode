from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        k = 0
        while k < n:
            ans += [i ^ (1<<k) for i in ans[::-1]]
            k += 1
        return ans

'''
[0]
k = 0
00 ^ 01 = 01
[0, 1]

k = 1
01 ^ 10 = 11
00 ^ 10 = 10
[0, 1, 3, 2]

k = 2
010 ^ 100 = 110
011 ^ 100 = 111
001 ^ 100 = 101
000 ^ 100 = 100
[0,1,3,2,6,7,5,4]
'''