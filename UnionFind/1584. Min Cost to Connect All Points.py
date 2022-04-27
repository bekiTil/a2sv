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
        if parent1==parent2:
            return False
        if self._rank[parent1]>self._rank[parent2]:
            self._parent[parent2]=parent1
            self._rank[parent1]+=1
        else:
            self._parent[parent1]=parent2
            self._rank[parent2]+=1
        return True 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        new=[]
        def dist(p,q):
            return abs(p[0]-q[0])+abs(p[1]-q[1])
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                value=dist(points[i],points[j])
                new.append([value,i,j])
        
        new.sort()
        mini=UnionFind(len(points))
      
        ans=0
        for i in new:
            if mini.union(i[1],i[2]):
                ans+=i[0]
            else:
                pass
        print(ans)
        return ans 
                
                
        
