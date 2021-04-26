class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        p = sorted(list(p))
        left, right = 0, len(p)
        while right <= len(s):
            cur_s = s[left:right]
            if sorted(list(cur_s)) == p:
                answer.append(left)
                
            left += 1
            right += 1
        return answer