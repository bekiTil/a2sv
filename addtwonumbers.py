# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new=""
        news=""
        while l1!=None:
            new+=str(l1.val)
            l1=l1.next
        while l2!=None:
            news+=str(l2.val)
            l2=l2.next
        new=new[::-1]
        news=news[::-1]
        new=int(new)
        news=int(news)
        sums=new + news
        sums=[int(x) for x in str(sums)]
        sums.reverse()
        head=None
        for i in range(len(sums)-1,-1,-1):
            current=ListNode(sums[i],head)
            head=current
        return head
