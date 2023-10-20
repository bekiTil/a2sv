class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans=0
        stack=[-1]
        maximum=0
        prev=0
        last=False
        for index,i in enumerate(s):
            if i=="(":
                stack.append(index)
            else:
                value=stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    maximum=max(maximum,index-stack[-1])
        return maximum
        