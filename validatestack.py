class Solution(object):
    def validateStackSequences(self, pushed, popped):
        check=[]
        new=[]
        ne=0
        popped.reverse()
        n=len(popped)-1
        while len(popped)!=n and len(popped)!=0:
            n=len(popped)
            i=0
            j=0
            while i<(len(pushed)-len(check)):
                if ne==0:
                    new.append(pushed[j])
                
                while  i>-1 and new[i]==popped[-1]:
                    check.append(popped.pop())
                    new.pop()
                    i-=1    
                i+=1
                j+=1
            ne+=1
        if len(popped)==0:
            return True
        else:
            return False
            
                    
