class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree=[0]*numCourses
        neighbour=defaultdict(set)
        for dep,ind in prerequisites:
            degree[dep]+=1
            neighbour[ind].add(dep)
        
        new=deque()
        for node in range(len(degree)):
            if degree[node]==0:
                new.append(node)
        
        ans=[]
        while new:
            value=new.popleft()
            ans.append(value)
            for i in neighbour[value]:
                degree[i]-=1
                if degree[i]==0:
                    new.append(i)
        if len(ans)!=numCourses:
            return []
        else:
            return ans 
                    
