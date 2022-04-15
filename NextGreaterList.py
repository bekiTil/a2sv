# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        check=head
        stack=[]
        new=[]
        while check!=None:
            stack.append(check.val)
            check=check.next
        value=[0]*len(stack)
        for i in range(len(stack)-1,-1,-1):
            if not new:
                new.append(stack[i])
            elif new[-1]>stack[i]:
               
                value[i]=new[-1]
                new.append(stack[i])
            else:
                
                while new and new[-1]<=stack[i]:
                    new.pop()
                if new:
                    value[i]=new[-1]
                new.append(stack[i])
                
       
                
        
        return value
                
