class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        reverses=[]
        for i in s:
            if i=="(":
                reverses.append(len(stack))
            elif i==")":
                j=reverses[-1]
                k=len(stack)-1
                while j<k:
                    stack[j],stack[k]=stack[k],stack[j]
                    j+=1
                    k-=1
                reverses.pop()
            else:
                stack.append(i)
        return "".join(stack)
                    
        
