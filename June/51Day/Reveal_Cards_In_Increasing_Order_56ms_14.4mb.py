from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = []
        deck.sort(reverse=True)
        for n in deck:
            if not answer:
                answer.append(n)
                continue
            tmp = answer.pop()
            answer = [n] + [tmp] + answer
        return answer