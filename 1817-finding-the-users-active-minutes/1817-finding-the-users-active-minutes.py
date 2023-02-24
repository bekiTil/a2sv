class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0]*k
   
        memo = {}

        #O(lenOfLogs)
        for log in logs:
            if log[0] not in memo:
                memo[log[0]] = {log[1]}
            else:
                memo[log[0]].add(log[1])

        
        for key,value in memo.items():
            total = len(value)
            answer[total-1]+=1

        return answer