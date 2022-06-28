#Time Complexity O(n) for all operation 
#Space Complexity O(n) for all operation 

class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.node=Node()

    def get(self, index: int) -> int:
        head=self.node
        ind=0
        if head.val==None:
            return -1 
        while head:
            if ind==index:
                return head.val
            head=head.next
            ind+=1
        return -1

    def addAtHead(self, val: int) -> None:
        head=self.node
        if head.val==None:
            head.val=val
        else:
            self.node=Node(val,head)


    def addAtTail(self, val: int) -> None:
        head=self.node
        if head.val==None:
            head.val=val
        else:
            while head.next:
                head=head.next
            head.next=Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        head=self.node
        ind=1
        if ind-1==index:
            self.node=Node(val,head)
        while head:
            if ind==index:
                head.next=Node(val,head.next)
                break
            head=head.next
            ind+=1
        

    def deleteAtIndex(self, index: int) -> None:
        head=self.node
        ind=1
        if ind-1==index:
            if head.next==None:
                self.node=Node()
            else:
                self.node=Node(head.next.val,head.next.next)
        while head:
            if ind==index:
                if head.next!=None:
                    head.next=head.next.next
                    break
            head=head.next
            ind+=1
        
            
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
