# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new=head
        while new!=None:
            if new.next==None:
                break
            while (new.val==new.next.val):
                new.next=new.next.next
                if new.next==None:
                    break
            new=new.next
        return head
        print(head)
        
