class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        new={}
        for i in range(len(s)):
            if s[i] in new:
                if new[s[i]]!=t[i]:
                    return False
            else:
                if t[i] not in new.values():
                    new[s[i]]=t[i]
                else:
                    return False
                   
        return True
                