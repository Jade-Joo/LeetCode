from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        itst = Counter(s) - Counter(t)
        return sum(itst.values())