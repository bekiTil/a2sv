class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit=[]
        letter=[]
        for m in logs:
            temp=m.split()
            for i in temp[1:]:
                if i.isdigit():
                    digit.append(m)
                else:
                    letter.append((temp[1:],m))
                break
        letter.sort()
        res=[]
        for i in letter:
            res.append(i[1])
        res.extend(digit)
        return res