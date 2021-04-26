class Solution:
    def dfs(self, row, col, board, word, temp, idx):
        if idx == len(word):
            return True

        for nxt_row, nxt_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if nxt_row < 0 or nxt_row >= len(board) or nxt_col < 0 or nxt_col >= len(board[0]) or (nxt_row, nxt_col) in temp:
                continue
            if board[nxt_row][nxt_col] == word[idx]:
                if self.dfs(nxt_row, nxt_col, board, word, temp + [(nxt_row, nxt_col)], idx + 1):
                    return True
        else:
            return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, board, word[1:], [(i, j)], 0):
                        return True
        else:
            return False