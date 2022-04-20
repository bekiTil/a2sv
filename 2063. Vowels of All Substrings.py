class Solution:
    def countVowels(self, word: str) -> int:
        i=0
        sums=0
        last=0
        vowels=set(("a","e","i","o","u"))
        while i<len(word):
            if word[i] in vowels:
                last+=1
                sums+=last
            else:
                sums+=last
            i+=1
        
        length=len(word)
        temp=sums
    
        for i in range(1,len(word)):
            if word[i-1] in vowels:
                temp-=(length)
                length-=1
                sums+=temp
            else:
                sums+=temp
                length-=1
        return sums
