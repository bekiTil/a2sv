# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter=1
        new=head
        past=head
        number=0
        while new!=None:
            new=new.next
            number+=1
        node=(number-n)+1
        
        prev=None
        
        while counter < node :
            prev=past
            past=past.next
            
            counter+=1
        if counter==1:
            return head.next
        
        prev.next=past.next
        
        return head
