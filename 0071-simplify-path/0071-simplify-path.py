class Solution:
    def simplifyPath(self, path: str) -> str:
        value=path.split("/")
        
        start=["/"]
        for i in value:
            if i=="" or i==".":
                pass
            elif i=="..":
                if start:
                    start.pop()
                if start and start[-1]=="/":
                    start.pop()
            else:
                if start and start[-1]!="/":
                    start.append("/")
                elif not start:
                     start.append("/")
                start.append(i)
        if not start:
            start.append("/")
        return "".join(start)
        