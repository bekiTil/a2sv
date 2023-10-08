class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort(reverse=True)
        processorTime.sort()
        index = 0
        ans = 0
        for val in processorTime:
            ans = max(val+tasks[index],ans)
            index+=4
        return ans