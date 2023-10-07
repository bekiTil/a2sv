# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        reminder  = 0
        while l1 or l2:
            temp = 0
            if l1:
                temp+= l1.val
                l1= l1.next
            if l2:
                temp += l2.val
                l2 = l2.next
            dummy.next= ListNode((temp+reminder)%10)
            dummy= dummy.next
            reminder = (temp+reminder)//10
        if reminder>0:
            dummy.next = ListNode(reminder)
        return ans.next
            