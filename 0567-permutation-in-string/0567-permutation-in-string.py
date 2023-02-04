class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count=defaultdict(int)
        for i in s1:
            count[i]+=1
        val=set(s1)
        tempcount=defaultdict(int)
        i=0
        length=0
        for index,k in enumerate(s2):
          
            if k not in val:
                tempcount,length,i=defaultdict(int),0,index+1
                continue
            
            tempcount[k]+=1
            
                
           
            while i<len(s2) and tempcount[k]>count[k]:
                tempcount[s2[i]]-=1
                length-=1
                i+=1
                
            if tempcount[k]<=count[k]:
                length+=1
            if length==len(s1):
                return True
            
            