class Solution:
    def decodeString(self, s: str) -> str:
        storenum=[]
        num=[]
        temp=''
        string=[]
        i=0
        while i < len(s):
            
            if s[i].isdigit():
                temp=''
                temp+=s[i]
                i+=1
                while i <len(s):
                    if s[i].isdigit():
                        temp+=(s[i])
                        i+=1
                    else:
                        break
                num.append(int(temp))
                print(num)
            elif s[i]=="[":
                storenum.append(len(string))
                i+=1
            elif s[i]=="]":
                j=storenum[-1]
                k=len(string)
                new=num[-1]*string[j:k]
                storenum.pop()
                num.pop()
                del string[j:]
                string.extend(new)
                i+=1
            else:
                string.append(s[i])
                i+=1
        
        return "".join(string)
                
