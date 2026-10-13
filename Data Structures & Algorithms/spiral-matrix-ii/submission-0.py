class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0]*n for i in range(n)]

        def outline(start, k):
            nonlocal val
            for c in range(start, start + k):
                matrix[start][c] = val
                val += 1
            for r in range(start+1, start + k):
                matrix[r][start + k - 1] = val
                val +=1
            for c in range(start+k-2, start-1, -1):
                matrix[start+k-1][c] = val
                val +=1
            for r in range(start+k-2, start, -1):
                matrix[r][start] = val
                val +=1

        val = 1
        k = len(matrix)
        seen = set()
        for root in range((n+1)//2):
            outline(root, k)
            k-= 2
        
        return matrix


