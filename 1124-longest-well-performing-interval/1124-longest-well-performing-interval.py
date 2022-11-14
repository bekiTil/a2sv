class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        prefix=[0]
        
        for i in hours:
            if i>8:
                prefix.append(prefix[-1]+1)
            else:
                prefix.append(prefix[-1]-1)
        count={}
        maximum=0
        
        for i in range(len(prefix)):
            if prefix[i]>0:
                maximum=i
            if prefix[i] not in count:
                count[prefix[i]]=i
            
            if prefix[i]-1 in count:
                maximum=max(maximum,i-count[prefix[i]-1])
        return maximum