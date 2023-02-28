class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        maximum  = 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                matrix[i][j] = int(matrix[i][j])
                right, bottom, bottomRight = 0 ,0 , 0 
                if j<n-1:
                    right = matrix[i][j+1]
                
                if i<m-1:
                    bottom = matrix[i+1][j]
                
                if j< n-1 and i<m-1:
                    bottomRight = matrix[i+1][j+1]
                
                if matrix[i][j] != 0:
                    matrix[i][j] = min(right, bottom, bottomRight) + 1
                
                maximum = max(maximum, matrix[i][j])

        return maximum**2
        
