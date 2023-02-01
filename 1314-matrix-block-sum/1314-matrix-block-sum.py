class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        dp=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            dp[i][0]=mat[i][0]
            for j in range(1,len(mat[0])):
                dp[i][j]+=dp[i][j-1]+mat[i][j]
       
        for i in range(1,len(mat)):
            for j in range(len(mat[0])):
                dp[i][j]+=dp[i-1][j]
       
        ans=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                min_x,max_x=i-k,i+k
                min_y,max_y=j-k,j+k
               
                if max_x>=len(mat):
                    max_x=len(mat)-1
                if max_y>=len(mat[0]):
                    max_y=len(mat[0])-1
                if min_x<0:
                    min_x=0
                if min_y<0:
                    min_y=0
                # print((i,j),(max_x,max_y),(min_x,min_y))
                ans[i][j]+=dp[max_x][max_y]
                if min_y-1>=0 and min_x-1>=0:
                    ans[i][j]+=dp[min_x-1][min_y-1]
                if min_y-1>=0:
                    ans[i][j]-=dp[max_x][min_y-1]
                if min_x-1>=0:
                    ans[i][j]-=dp[min_x-1][max_y]
        
        return ans
                