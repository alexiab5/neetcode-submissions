class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        while i <= j:
            mid = (i + j) // 2
            if target < matrix[mid][m - 1]:
                j = mid - 1
            elif target > matrix[mid][m - 1]:
                i = mid + 1
            else:
                return True
        
        if i < 0 or i > n - 1:
            return False
        
        row = i
        i, j = 0, m - 1
        while i <= j:
            mid = (i + j) // 2
            if target < matrix[row][mid]:
                j = mid - 1
            elif target > matrix[row][mid]:
                i = mid + 1
            else:
                return True

        return False