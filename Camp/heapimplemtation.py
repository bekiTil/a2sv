 class Solution:
    #Heapify function to maintain heap property.
    def leftChild(self,i):
        return 2*i+1
    def rightChild(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def upheap(self,arr,n,i):
        if i>0 and arr[self.parent(i)]>arr[i]:
            arr[self.parent(i)],arr[i]=arr[i],arr[self.parent(i)]
            self.upheap(arr,n,self.parent(i))
    def downheap(self,arr,n,i):
        l=self.leftChild(i)
        r=self.rightChild(i)
        if l<n and arr[l]<arr[i]:
            small=l
        else:
            small=i
        if r<n and arr[r]<arr[small]:
            small=r
        if small!=i:
            arr[i],arr[small]=arr[small],arr[i]
            self.downheap(arr,n,small)
    def heapify(self,arr, n, i):
        # code here
        self.upheap(arr,n,i)
        self.downheap(arr,n,i)
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(len(arr)):
            self.heapify(arr,n,i)
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        for i in range(n-1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
        arr.reverse()
