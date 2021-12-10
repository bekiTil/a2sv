def insertionSort1(n, arr):
    # Write your code here
    new=arr[n-1]
    j=n-2
    while j>=0:
        if arr[j]>new:
            arr[j+1]=arr[j]
            for i in arr:
                print(i,end=" ")
            print()
        else:
            arr[j+1]=new
            for i in arr:
                print(i,end=" ")
            break
        j=j-1
