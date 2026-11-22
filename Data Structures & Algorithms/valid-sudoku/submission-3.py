class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            digits = [0 for _ in range(10)]
            for j in range(n):
                if board[i][j] != '.':
                    curr = int(board[i][j])
                    if digits[curr] == 1:
                        return False
                    digits[curr] = 1
        
        for j in range(n):
            digits = [0 for _ in range(10)]
            for i in range(n):
                if board[i][j] != '.':
                    curr = int(board[i][j])
                    if digits[curr] == 1:
                        return False
                    digits[curr] = 1
        
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                digits = [0 for _ in range(10)]
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] != '.':
                            curr = int(board[x][y])
                            if digits[curr] == 1:
                                return False
                            digits[curr] = 1
        return True