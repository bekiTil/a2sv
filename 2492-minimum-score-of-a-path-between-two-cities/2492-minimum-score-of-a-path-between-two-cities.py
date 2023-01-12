class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i,j,value in roads:
            graph[i].append((j,value))
            graph[j].append((i,value))
            
        level=deque([])
        level.append(1)
        visited=set()
        minimum=float("inf")
        visited.add(1)
        while level:
            length=len(level)
            for _ in range(length):
                value=level.popleft()
                for i,val in graph[value]:
                    if i not in visited:
                        level.append(i)
                        visited.add(i)
        for i,j,value in roads:
            if i in visited and j in visited:
                minimum=min(minimum,value)
        return minimum
        
       