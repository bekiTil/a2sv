class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        num=[]
        k=0
        for i in s:
            num.append((int(i[-1])-1))
            i=i[:-1]
            num.append(i)
            
            k+=1
        for i in range(0,len(num)-1,2):
                  s[num[i]]=num[i+1]     
        return " ".join(s)
            
            
