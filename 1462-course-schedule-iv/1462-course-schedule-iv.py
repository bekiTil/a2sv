class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n=numCourses
        arr=[[float("inf") for _ in range(numCourses)] for _ in range(numCourses)]
        
        for i in range(n):
            arr[i][i]=0
        for i,j in prerequisites:
            arr[i][j]=1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    arr[i][j]=min(arr[i][j],arr[i][k]+arr[k][j])
        # for val in arr:
        #     print(*val)
        ans=[]
        for i,j in queries:
            if arr[i][j]!=float("inf"):
                ans.append(True)
            else:
                ans.append(False)
        return ans
            
                