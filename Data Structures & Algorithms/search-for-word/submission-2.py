class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search_word(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if word[k] != board[i][j] or board[i][j] == '#':
                return False
            if k == len(word) - 1:
                return True

            board[i][j] = '#'
            res = search_word(i + 1, j, k + 1) or search_word(i - 1, j, k + 1) or search_word(i, j + 1, k + 1) or search_word(i, j - 1, k + 1)
            board[i][j] = word[k]
            return res
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search_word(i, j, 0):
                    return True
        
        return False