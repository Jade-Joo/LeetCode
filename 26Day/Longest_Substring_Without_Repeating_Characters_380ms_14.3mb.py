class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:  
#         used = {}
#         max_length = start = 0
#         for i, c in enumerate(s):
#             if c in used and start <= used[c]:
#                 start = used[c] + 1
#             else:
#                 max_length = max(max_length, i - start + 1)

#             used[c] = i
#             print(used)

#         return max_length
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == len(set(s)):
            return len(s)
        
        answer = 0
        for i in range(len(s)):
            cur_word = s[i]
            for j in range(i + 1, len(s)):
                nxt_word = s[j]
                if nxt_word in cur_word:
                    break
                else:
                    cur_word += nxt_word

            answer = max(answer, len(cur_word))
        return answer