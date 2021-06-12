from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def convert(s):
            tmp = {}
            res = ''
            ascii = 64
            for i in s:
                if i not in tmp:
                    ascii += 1
                    tmp[i] = chr(ascii)
                    res += chr(ascii)
                else:
                    res += tmp[i]

            return res
        
        p = convert(pattern)

        answer = []
        for word in words:
            conv_word = convert(word)

            if conv_word == p:
                answer.append(word)
        return answer