class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        
        result=1
        
        print(pairs)
        prev=pairs[0][1]
        for i in pairs[1:]:
            if prev<i[0]:
                
                prev=i[1]
                result+=1
        return result
            
        