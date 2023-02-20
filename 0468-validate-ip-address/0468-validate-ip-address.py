class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        temp = queryIP.split(".")
        value = queryIP.split(":")
        
        upper =['a','b','c','d','e','f']
        lower = ['A', 'B', 'C','D' , 'E' , 'F']
        if len(temp)== 4:
            for val in temp:
                if not val.isdigit() or (val[0]=="0" and len(val)>1) or int(val)>255:
                    return "Neither"
            return "IPv4"
        
            
        elif len(value)== 8:
            
            for val in value:
                if len(val)> 4 or len(val)<1:
                    return 'Neither'
                for char in val:
                    if not (char.isdigit() or char in upper or char in lower ) :
                        return 'Neither'
            return  'IPv6'
                
            
        else:
            return "Neither"
      
        