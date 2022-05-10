class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        new1=version1.split(".")
        new2=version2.split(".")
        i=0
        j=0
        while i<len(new2) and j<len(new1):
            if int(new2[i])>int(new1[j]):
                return -1
            elif int(new2[i])<int(new1[j]):
                return 1
            else:
                i+=1
                j+=1
        if len(new1)==len(new2):
            return 0
        elif  len(new1)>len(new2):
            value=0
            for m in new1[j:]:
                value+=int(m)
            if value==0:
                return 0
            else:
                return 1
        else:
            value=0
            for k in new2[i:]:
                value+=int(k)
            if value==0:
                return 0
            else:
                return -1
