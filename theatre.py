import math
def theatre():
    new = list(map(int, input().split()))
    x=math.ceil(new[0]/new[2])
    y=math.ceil(new[1]/new[2])
    print(x*y)
