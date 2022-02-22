# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new=[]
        
        for i in (lists):
            while i!=None:
                new.append(i.val)
                i=i.next
        print(new)
        hq.heapify(new)
        print(new)
        head=None
        if len(new)==0:
            return None
        while len(new)!=0:
            news=ListNode(hq.heappop(new),head)
            head=news
        heads=None
        current=news
        while current!=None:
            nexts=current.next
            current.next=heads
            heads=current
            current=nexts
        current=heads
        return current
        
        
        
            
