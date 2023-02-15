class Solution:
    def checkValidString(self, s: str) -> bool:
        stack =[]
        stack2 = []
		
        for i,char in enumerate(s):
            if char == "(": 
                stack.append(i)
            elif char == ")":
                if not stack and not stack2: 
                    return False
                elif stack:
                    stack.pop()
                elif stack2: 
                    stack2.pop()
            else: 
                stack2.append(i)
    
        while stack:
            if stack2 and stack[-1] < stack2[-1]:
                stack.pop()
                stack2.pop()
            else:
                if not stack2: 
                    return False
                else:
                    stack2.pop()
				
        return True
        