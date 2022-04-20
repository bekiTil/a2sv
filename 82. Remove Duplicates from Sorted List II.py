# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new=head
        unique=[]
        memo={}
        while new:
            if new.val in memo:
                memo[new.val]+=1
            else:
                memo[new.val]=1
            new=new.next
        
        
        for i in memo:
            if memo[i]==1:
                unique.append(i)
        
        node=None
        temp=None
        while unique:
            node=ListNode(unique.pop(),temp)
            temp=node
        
        return node
