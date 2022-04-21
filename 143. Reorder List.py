# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp=None
        revers=head
        while revers:
            new=ListNode(revers.val,temp)
            temp=new
            revers=revers.next
        stack=deque([])
        
        fine=head.next
        check=True
        
        while fine and new:
            if check:
                stack.append(fine.val)
                fine.val=new.val
                check=False
                fine=fine.next
                new=new.next
            else:
                temp=stack.popleft()
                stack.append(fine.val)
                fine.val=temp
                fine=fine.next
            
                check=True
