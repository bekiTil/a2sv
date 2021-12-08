class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        newlists=[]
        for i in range(1,n+1):
            if (i)%3==0 and (i)%5==0:
                newlists.append("FizzBuzz")
            elif (i)%3==0 :
                newlists.append("Fizz")
            elif  (i)%5==0 :
                newlists.append("Buzz")
            else:
                newlists.append(str(i))
        return newlists
