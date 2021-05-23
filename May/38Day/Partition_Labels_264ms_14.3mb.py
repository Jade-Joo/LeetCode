'''
Union time complextity = O(len(s)+len(t))
'''
class Solution:
    def partitionLabels(self, S):
        sizes = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]): # 중복되는 값이 없으면 하나의 파티션이 나눠진 것
                i += 1
            sizes.append(i)
            S = S[i:]
        return sizes