'''
<output>
[0, 1]
[0, 1, 1, 2]
'''
class Solution(object):
    def countBits(self, num):
        res = [0]
        while len(res) <= num:
            res += [i + 1 for i in res] # 이전 값들에 1을 더해준 값들이 다음에 오는 countbits이다.
        return res[:num + 1]