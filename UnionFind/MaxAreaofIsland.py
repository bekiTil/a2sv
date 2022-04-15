class UnionFind:
    def __init__(self,n):
        self._parent=[node for node in range(n)]
        self._rank=[1 for _ in range(n)]
        
    def find(self,number):
        if self._parent[number]==number:
            return number
        self._parent[number]= self.find(self._parent[number]) 
        return self._parent[number]
    def rank(self,number):
        return self._rank[number]
    def union(self,node1,node2):
        parent1=self.find(node1)
        parent2=self.find(node2)
        if self._rank[parent1]>self._rank[parent2]:
            self._parent[parent2]=parent1
            self._rank[parent1]+=1
        else:
            self._parent[parent1]=parent2
            self._rank[parent2]+=1
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        new=UnionFind(m*n)
        dxn=[(0,1),(1,0),(-1,0),(0,-1)]
       
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    continue
                for d in dxn:
                    x,y=d
                    x,y=i+x,j+y
                    if 0<=x<n and 0<=y<m and grid[x][y]==1:
                        new1=i*m+j
                        new2=x*m+y
                        
                        new.union(new1,new2)
       
        
        memo={}
       
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    continue
                new1=i*m+j
                parent=new.find(new1)
                if parent in memo:
                    memo[parent]+=1
                else:
                    memo[parent]=1
        maxi=float("-inf")
        for key in memo:
            maxi=max(memo[key],maxi)
        return maxi if maxi!=float("-inf") else 0
