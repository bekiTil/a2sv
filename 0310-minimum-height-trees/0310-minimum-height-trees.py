class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        memo=defaultdict(int)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        def bfs1(value):
            visited=set()
            visited.add(value)
            level=deque([value])
            while level:
                temp=level[0]
                for _ in range(len(level)):
                    value=level.popleft()
                    for val in graph[value]:
                        if val not in visited:
                            visited.add(val)
                            level.append(val)
                
            return temp
        first_value=bfs1(0)
        second_value=bfs1(first_value)
        def bfs2(value):
            visited=set()
            visited.add(value)
            level=deque([value])
            length=1
            while level:
                for _ in range(len(level)):
                    node=level.popleft()
                    for val in graph[node]:
                        if val not in visited:
                            visited.add(val)
                            level.append(val)
                            memo[(value,val)]=length
                length+=1
        bfs2(first_value)
        bfs2(second_value)
        mini=float("inf")
        for i in range(n):
            mini=min(max(memo[(first_value,i)],memo[(second_value,i)]),mini)
        ans=[]
        for i in range(n):
            if max(memo[first_value,i],memo[(second_value,i)])==mini:
                ans.append(i)
        return ans
                    