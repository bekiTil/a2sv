def countingSort(arr):
    # Write your code here
    max=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>max:
            max=arr[i]
    new=[0]*(max+1)
    
    for i in arr:
        new[i]+=1
    return new
