class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans = 0
        for val in words:
            
            first = 0
            value = 0
            index  = 0
            count = 0 
            find = True
            while index < len(val) and value < len(s):
                # print(index,value)
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
               
            
            if not ( (temp == count) or (temp > count and temp>=3)):
                    find=False
            if len(set(val))!= len(set(s)):
                find=False
            
            if value < len(s):
                find = False
            if find:
                ans +=1
        return ans
          