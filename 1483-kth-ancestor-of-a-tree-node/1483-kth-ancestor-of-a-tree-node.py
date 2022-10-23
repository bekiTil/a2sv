class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.ans=parent
        self.graph=defaultdict(list)
        self.parent={}
        self.visited=set()
        self.binary=defaultdict(int)
        self.depth=defaultdict(int)
        def dfs(node,value):
            for i in self.graph[node]:
                if i not in self.visited:
                    self.parent[i]=node
                    self.visited.add(i)
                    dfs(i,value+1)
            self.depth[node]+=value
                    
        def binary_jumping(node,k):
            if k==0:
                return 
            elif k==1:
                self.binary[(node,k)]=self.parent[node]
                return self.parent[node]
            elif (node,k) in  self.binary:
                return self.binary[(node,k)]
            else:
                value=binary_jumping(node,k//2)
                self.binary[(node,k)]=binary_jumping(value,k//2)
                return self.binary[(node,k)]
             
       
        for index,i in enumerate(self.ans):
            if i!=-1:
                self.graph[i].append(index)
        self.visited.add(0)
        dfs(0,0)
        for i in range(n):
            if self.depth[i]!=0:
                binary_jumping(i,pow(2,floor(log(self.depth[i])/log(2))))      
        
        
    def getKthAncestor(self, node: int, k: int) -> int:
        if k>self.depth[node]:
            return -1
        while k>0:
            dps = int(math.log2(k))
            k -= pow(2, dps)
            node=self.binary[(node,pow(2,dps))]
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)