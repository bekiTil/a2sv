# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        check=head
        ans=head
        length=0
        
        while check!=None:
            length+=1
            check=check.next
        j=0
        while j<length//2:
            ans=ans.next
            j+=1
       
        next=None
        while ans:
            new=ListNode(ans.val,next)
            next=new
            ans=ans.next
        maxi=float("-inf")
        while new:
            maxi=max(head.val+new.val,maxi)
            head=head.next
            new=new.next
        
        return maxi
            
