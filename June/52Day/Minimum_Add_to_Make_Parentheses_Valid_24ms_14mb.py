class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        tmp = []
        for i in s:
            if not tmp:
                tmp.append(i)
                continue
            if tmp[-1] == "(" and i == ")":
                tmp.pop()
            else:
                tmp.append(i)
        return len(tmp)