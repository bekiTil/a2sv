#Time Complexity O(m*n) where m is the number of rotation and n is the length of linked list
#Space Complexity O(n) as i used extra space to store the rotated linked list for the answer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head
        rotate=0
        checker=head
        length=0
        while checker:
            checker=checker.next
            length+=1
        if length<=k:
            k=k%length
        
        while rotate<k:
            new=head
            while new.next.next:
                new=new.next
            changed=new.next.val
            new.next=None
            news=ListNode(changed,head)
            head=news
            rotate+=1
        return head
