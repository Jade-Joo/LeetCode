class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(path, word):
            if path not in res:
                if path:
                    res.add(path)
                for i in range(len(word)):
                    dfs(path + word[i], word[:i] + word[i + 1:])
            
        dfs('', tiles)
        return len(res)