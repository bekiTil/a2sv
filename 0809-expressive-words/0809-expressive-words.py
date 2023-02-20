class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for val in words:
            first , value , index , find = 0 , 0 , 0 , True
            
            while index < len(val) and value < len(s):
               
                count = 0
                while index < len(val):
                    if val[index] == val[first]:
                        count +=1
                        
                    else:
                        break
                    index +=1
                temp = 0
                while value < len(s):
                    if val[first] == s[value]:
                        temp +=1
                    else:
                        break
                    value +=1 
                first = index
                if not ( (temp == count) or (temp > count and temp>=3)):
                    find=False
                    break
            
            if value < len(s) or index < len(val):
                find = False
            if find:
                ans +=1
        return ans
          