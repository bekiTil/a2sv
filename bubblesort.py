def countSwaps(a):
    # Write your code here
    num=0
    for i in range(len(a)):
        for j in range(1,len(a)-i):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                num+=1
    print("Array is sorted in %d swaps." %(num))
    print("First Element: %d" %(a[0]))
    print("Last Element: %d" %(a[-1]))
