class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numstack =[]
        curNum = 0
        for char in s:
            if char.isdigit():
                curNum=curNum*10 + int(char)
                
            elif char == ']':
                tempstring = ''
                while stack[-1]!= '[':
                    tempstring+=stack.pop()[::-1]
                tempstring = tempstring[::-1]
                stack.pop()
                count = numstack.pop()
                stack.append(tempstring * count)
            else:
                if char== '[':
                    numstack.append(curNum)
                    curNum = 0
                stack.append(char)
            print(stack)
            print(numstack)
        return ''.join(st for st in stack)
       