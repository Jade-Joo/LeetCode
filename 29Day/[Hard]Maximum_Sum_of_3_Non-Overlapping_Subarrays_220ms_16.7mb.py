from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        #k 길이만큼 슬라이딩 윈도우 방식으로 합을 W에 저장
        W = [] #array of sums of windows
        curr_sum = 0
        for i, x in enumerate(nums):
            curr_sum += x
            if i >= k: 
                curr_sum -= nums[i - k]
            if i >= k - 1: 
                W.append(curr_sum)

        #오른쪽으로 이동하며 큰 값의 인덱스를 업데이트
        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        
        #왼쪽으로 이동하며 큰 값의 인덱스를 업데이트
        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best


        #k 길이인 3개의 subarray들의 합을 비교하며 가장 큰 값을 return
        #left와 right 리스트를 사용함으로서 사전순으로 값이 도출됨
        ans = [0, 0, 0]
        for j in range(k, len(W) - k):
            i, l = left[j - k], right[j + k]
            if ans == [0] * 3 or (W[i] + W[j] + W[l] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = [i, j, l]

        return ans