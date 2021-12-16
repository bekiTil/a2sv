   def isValid(self, s: str) -> bool:
        dic={"{":"}","[":"]","(":")"}
        stack=[]
        for i in s:
            
            if i in dic.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                poped=stack.pop()
                if i !=dic[poped]:
                    return False
        
        return len(stack)==0
