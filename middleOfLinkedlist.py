# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        reserver=head
        while(head != None):
            n+=1
            head = head.next
        new=n//2
        checker=0
        printed=ListNode()
        while (reserver!=None):
            checker+=1
            if checker>new:
                printed.val=reserver.val
                printed.next=reserver.next
                break
            reserver=reserver.next
        return printed
