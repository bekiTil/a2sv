class UnionFind:
    def __init__(self,n):
        self._parent=[node for node in range(n)]
        self._rank=[1 for _ in range(n)]
        
    def find(self,number):
        if self._parent[number]==number:
            return number
        self._parent[number]= self.find(self._parent[number]) 
        return self._parent[number]
        
    def union(self,node1,node2):
        parent1=self.find(node1)
        parent2=self.find(node2)
        if self._rank[parent1]>self._rank[parent2]:
            self._parent[parent2]=parent1
            self._rank[parent1]+=1
        else:
            self._parent[parent1]=parent2
            self._rank[parent1]+=1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        new=UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i!=j and isConnected[i][j]==1:
                    new.union(i,j)
        news=set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    parent=new.find(i)
                    news.add(parent)
        return len(news)
                    
