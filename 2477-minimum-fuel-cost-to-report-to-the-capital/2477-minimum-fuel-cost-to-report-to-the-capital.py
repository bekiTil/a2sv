class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph=defaultdict(list)
        
        for i,j in roads:
            graph[i].append(j)
            graph[j].append(i)
        visited=set()
        visited.add(0)
        def dfs(root,seats):
            current_person,num_of_cars,liters=1,1,0
            for val in graph[root]:
                if val not in visited:
                    visited.add(val)
                    new_person,new_num_of_cars,new_liters=dfs(val,seats)
                    liters+=(new_num_of_cars+new_liters)
                    num_of_cars+=new_num_of_cars
                    
                    if current_person+new_person>seats:
                        
                        current_person=current_person+new_person - seats
                    else:
                        current_person+=(new_person)
                        num_of_cars-=1
                   
            return current_person,num_of_cars,liters
        
        return dfs(0,seats)[-1]
                        