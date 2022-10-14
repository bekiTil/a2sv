# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        care=head
        ans=care
        n=0
        while care!=None:
            n+=1
            care=care.next
        
        middle=n//2
        
        check=0
        if check>middle-1:
            return head.next
        elif check==middle-1:
            ans.next=ans.next.next
        else:
            while check<middle-1:
                check+=1
                ans=ans.next
            ans.next=ans.next.next
        return head