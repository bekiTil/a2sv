class Solution:
    def calculate(self, s: str) -> int:
        operation=["*","/","+","-"]
        priority=["*","/"]
        secondary=["+","-"]
        stack=[]
        nestack=[]
        i=0
        news=""        
        while i <len(s):
           
            if s[i] in operation:
                stack.append(s[i])
            else:
               
                news+=s[i]
                if i+1!=len(s) and s[i+1] not in secondary and s[i+1] not in priority:
                    i+=1
                    continue
                else:
                    stack.append(int(news))
                    news=''
            i+=1
        
        i=0
        while i <len(stack):
            if stack[i] in priority: 
                if  stack[i]==priority[0]:
                    nestack[-1]=nestack[-1]*stack[i+1]
                    i+=1
                else:
                    nestack[-1]=nestack[-1]//stack[i+1]
                    i+=1
            else:
                nestack.append(stack[i])
            i+=1

        
        i=0
        stack=nestack
        nestack=[]
        while i<len(stack):
            if stack[i] in secondary:
                if  stack[i]==secondary[0]:
                    new=nestack[-1]+stack[i+1]
                    nestack.pop()
                    nestack.append(new)
                    i+=1
                else:
                    new=nestack[-1]-stack[i+1]
                    nestack.pop()
                    nestack.append(new)
                    i+=1
            else:
                nestack.append(stack[i])
            i+=1
        return nestack[0]
