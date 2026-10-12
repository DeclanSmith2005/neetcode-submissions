class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroCols = set()
        zeroRows = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroCols.add(c)
                    zeroRows.add(r)
        
        for r in zeroRows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        
        for r in range(len(matrix)):
            for c in zeroCols:
                matrix[r][c] = 0
                
        