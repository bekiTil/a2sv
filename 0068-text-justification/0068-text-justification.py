class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        index , length, ans = 0, len(words), []
        while index < length:
           
            line=[words[index]]
            j=index+1
            wordWidth=len(words[index])
            position=0
            space=maxWidth - len(words[index])
            while j<length and wordWidth + 1 + len (words[j])<=maxWidth:
                line.append(words[j])
                wordWidth += (1 + len(words[j]))
                space-=len (words[j])
                position, j =position +1,j+1
            index=j
                
            if index  < length and position:
                spaces=[" " * (space//position + (k< space % position)) for k in range(position) ]+ ['']
            else:
                spaces=[' ']* position + [' ' * (maxWidth - wordWidth)] 
            temp=[]
            for pair in zip (line,spaces):
                
                for s in pair:
                    temp.append(s)
            ans.append(''.join(temp))
                    
          
        return ans

        
