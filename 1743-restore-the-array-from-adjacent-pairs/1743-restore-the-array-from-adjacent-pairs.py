class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        inDegree =defaultdict(int)
        for val in adjacentPairs:
            a,b= val
            graph[a].append(b)
            graph[b].append(a)
            inDegree[a]+=1
            inDegree[b]+=1
        level=deque([])
        for val in inDegree:
            if inDegree[val]==1:
                level.append(val)
                visited=set()
                visited.add(val)
                break
        ans=[]
       
        while level:
            length=len(level)
          
            for _ in range(length):
                    num=level.popleft()
                    ans.append(num)
                    for adj in graph[num]:
                        inDegree[adj]-=1
                        if inDegree[adj]==1 or inDegree[adj]==0 and adj not in visited:
                            level.append(adj)
                            visited.add(adj)
        return ans
        