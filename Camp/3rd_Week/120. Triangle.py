#top_down approach
#time complexity O(m*n) where m is the height of the triangle where n is a variable width of the triangle
#Space Complexity O(m*n)
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
 
#bottom_up approach
#time complexity O(m*n) where m is the height of the triangle where n is a variable width of the triangle
#Space Complexity O(m*n)
  class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[0 for _ in range(j+1)]for j in range(len(triangle)+1)]
        for i in range(len(dp)-2,-1,-1):
            for j in range(len(dp[i])-1,-1,-1):
                dp[i][j]=min(triangle[i][j]+dp[i+1][j],triangle[i][j]+dp[i+1][j+1])
        return dp[0][0]
