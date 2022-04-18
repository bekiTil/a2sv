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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        new=UnionFind(len(accounts))
        i=0
        j=1
        while j<len(accounts):
            if accounts[i][0]==accounts[j][0]:
                for m in range(1,len(accounts[i])):
                    if accounts[i][m] in accounts[j]:
                        new.union(i,j)
                        
                        break
                j+=1
            else:
                j+=1
            if j>=len(accounts):
                i+=1
                j=i+1
        memo={}
        for i in range(len(accounts)):
            parent=new.find(i)
            if parent in memo:
                memo[parent].append(i)
            else:
                memo[parent]=[i]
        ans=[]
        for i in memo:
            
            ans.append([accounts[i][0]])
            temp=[]
            for j in memo[i]:
    
                temp.extend(accounts[j][1:])
            temp=list(set(temp))
            
            temp.sort()
            ans[-1].extend(temp)
        
        return ans 
