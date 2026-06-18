class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c = 0
        while c < len(matrix):
            row = matrix[c]
            if matrix[c][-1] < target:
                c+=1
                continue
            for r in row:
                if r == target:
                    return True
            c+=1
        return False