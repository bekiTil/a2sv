"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total=0
        def dfs(id,total):
            k=0
            while id!=employees[k].id:
                k+=1
            total+=employees[k].importance
            for i in employees[k].subordinates:
                total=dfs(i,total)
            return total
        k=0
        while id!=employees[k].id:
            k+=1
        total+=employees[k].importance
        for i in employees[k].subordinates:
            total=dfs(i,total)
        return total
