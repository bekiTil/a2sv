class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        List=[]
        for i in range(n):
            List.append([0]*n)
        for i,j,k,l in queries:
            List[i][j]+=1
            if l+1<len(List[0]):
                List[i][l+1]-=1
            if k+1<len(List):
                List[k+1][j]-=1
            if k+1<len(List) and l+1<len(List):
                List[k+1][l+1]+=1
     
        for i in range(len(List)):
            for j in range(1,len(List[0])):
                List[i][j]+=List[i][j-1]
        for j in range(len(List[0])):
            for i in range(1,len(List)):
                List[i][j]+=List[i-1][j]
                
        return List