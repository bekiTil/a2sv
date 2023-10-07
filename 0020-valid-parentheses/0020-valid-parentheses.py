class Solution:
    def isValid(self, s: str) -> bool:
        memo={"{":"}","[":"]","(":")"}
        stack=[]
        for i in s:
            if i in memo:
                stack.append(i)
            else:
                if not stack:
                    return False
                value = stack.pop()
                if memo[value]!= i:
                    return False
        if stack:
            return False
        return True