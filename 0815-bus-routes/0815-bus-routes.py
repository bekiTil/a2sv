class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for index, route in enumerate(routes):
            for j in route:
                graph[j].add(index)
                
        
        level = [(source, 0)]
        visited = set()
        visited.add(source)
        for stop, bus in level:
            if stop == target:
                return bus
            for i in graph[stop]:
                for j in routes[i]:
                    if j not in visited:
                        level.append((j, bus + 1))
                        visited.add(j)
                routes[i] = []  
        
        return -1