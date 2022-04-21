# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new=head
        new=new.next
        length=0
        while new:
            temp=head
            length+=1
            m=new.val
            j=0
            while j<length or  temp.val>m:
                if temp.val>m:
                    temp.val,m=m,temp.val
                
                temp=temp.next
                j+=1
            new.val=m
            new=new.next
        return head
    
        
        
        
