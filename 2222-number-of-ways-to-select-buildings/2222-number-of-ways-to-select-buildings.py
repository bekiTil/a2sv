class Solution:
    def numberOfWays(self, s: str) -> int:
        zero=[0]
        one=[0]
        for i in s:
            if i=="0":
                zero.append(zero[-1]+1)
                one.append(one[-1]+0)
            else:
                one.append(one[-1]+1)
                zero.append(zero[-1])
        solution=0
        for i in range(len(s)):
            if s[i]=="0":
                solution+=(one[i]*(one[-1]-one[i+1]))
            else:
                solution+=(zero[i]*(zero[-1]-zero[i+1]))
        print(solution)
        return solution
        