class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif j==len(triangle)-1:
                return triangle[j][i]
            else:
                left=triangle[j][i]+dfs(i,j+1)
                right=triangle[j][i]+dfs(i+1,j+1)
                memo[(i,j)]=min(left,right)
                return min(left,right)
        return dfs(0,0)
