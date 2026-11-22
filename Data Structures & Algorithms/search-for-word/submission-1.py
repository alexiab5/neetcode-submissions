class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def search_word(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if word[k] != board[i][j] or visited[i][j] == 1:
                return False
            if k == len(word) - 1:
                return True

            visited[i][j] = 1
            res = search_word(i + 1, j, k + 1) or search_word(i - 1, j, k + 1) or search_word(i, j + 1, k + 1) or search_word(i, j - 1, k + 1)
            visited[i][j] = 0
            return res
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search_word(i, j, 0):
                    return True
        
        return False