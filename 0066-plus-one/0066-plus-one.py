class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(str(x) for x in digits)
        
        value=int(s)+1
        se=[]
        for x in str(value):
            se.append(int(x))
       
        return se