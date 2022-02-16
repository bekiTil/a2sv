class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heads=None
        current=head
        while current!=None:
            nexts=current.next
            current.next=heads
            heads=current
            current=nexts
        current=heads
        return current
            
