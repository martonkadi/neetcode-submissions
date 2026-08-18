class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        start = 0
        end = len(matrix) - 1

        while start <= end:
            midRow = (end+start) // 2
            if target > matrix[midRow][0]:
                start = midRow + 1
            elif target < matrix[midRow][0]:
                end = midRow - 1
            else:
                return True
        start = 0
        if end < 0:
            return False
        row = end
        end = len(matrix[row]) - 1

        while start <= end:
            midEl = (end+start) // 2

            if target == matrix[row][midEl]:
                return True
            elif target > matrix[row][midEl]:
                start = midEl + 1
            else:
                end = midEl - 1
        return False
