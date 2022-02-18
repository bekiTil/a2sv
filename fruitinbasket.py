class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        stack=[]
        maxi=0
        if len(fruits)<=2:
            return len(fruits)
        i=0
        j=0
        k=-1
        while j<len(fruits):
            
            if len(stack)<2:
                if fruits[j] not in stack:
                    stack.append(fruits[j])
                j+=1
            else:
                if fruits[j] in stack:
                    if fruits[j-1]==fruits[j] and (k==-1 or k==i):
                        k=j-1
                    elif fruits[j-1]!=fruits[j]:
                        k=j
                    else:
                        pass        
                    j+=1
                else:
                    if (j-i)+1>maxi:
                        maxi=(j-i)
                    if k==-1:
                        i=j-1
                        stack.remove(fruits[i-1])
                        stack.append(fruits[j])
                        j+=1
                    else:
                        if k==i:
                            k=j-1
                        i=k
                        stack.remove(fruits[k-1])
                        stack.append(fruits[j])
                        j+=1
        return max(j-i,maxi)
