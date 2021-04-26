class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        stack = [0]
        
        cnt =  0
        visited = [True] + [False] * amount
        
        while stack:
            temp = []
            cnt += 1
            for add_coin in stack:
                for cur_coin in coins:
                    nxt_coin = add_coin + cur_coin
                    if nxt_coin == amount:
                        return cnt
                    elif nxt_coin > amount:
                        continue
                    elif not visited[nxt_coin]:
                        visited[nxt_coin] = True
                        temp.append(nxt_coin)
            stack = temp[:]
        return -1