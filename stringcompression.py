class Solution:
    def compress(self, chars: List[str]) -> int:
        first=0
        last=1
        s=""
        counter=1
        while last<len(chars):
            
            if chars[first]==chars[last]:
                counter+=1
                last+=1
            else:
                if counter==1:
                    s+=chars[first]
                    first+=1
                    last+=1
                else:
                    s+=chars[first]
                    s+=str(counter)
                    first=last
                    last+=1
                    counter=1
       
        if counter==1:
            s+=chars[first]
        else:
            s+=chars[first]
            s+=str(counter)
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)
