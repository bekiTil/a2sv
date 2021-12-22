def countingValleys(steps, path):
    # Write your code here
    n=0
    counter=0
    for i in path:
        if i=="U":
            if n==-1:
                counter+=1
            n+=1
        else:
            n-=1
    return counter
