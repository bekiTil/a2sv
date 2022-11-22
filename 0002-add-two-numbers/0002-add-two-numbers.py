# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode=ListNode(0)
        temporary=newNode
        add=0
        while l1 and l2:
            value=l1.val+l2.val+add
            add=0
            if value>=10:
                value-=10
                add=1
                
            newNode.next=ListNode(value)
            newNode=newNode.next
            l1=l1.next
            l2=l2.next
        # print(temporary)
        while l1:
            value=l1.val+add
            add=0
            if value>=10:
                value-=10
                add=1
            newNode.next=ListNode(value)
            newNode=newNode.next
            l1=l1.next
        while l2:
            value=l2.val+add
            add=0
            if value>=10:
                value-=10
                add=1
            newNode.next=ListNode(value)
            newNode=newNode.next
            l2=l2.next
        if add!=0:
            newNode.next=ListNode(1)
            
        return temporary.next