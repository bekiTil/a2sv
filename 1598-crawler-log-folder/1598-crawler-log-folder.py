class Solution:
    def minOperations(self, logs: List[str]) -> int:
        total = 0
        for log in logs: 
            if log=="./":
                continue
            elif log=="../":
                total=max(total-1,0)
            else:
                total+=1
        return total
        