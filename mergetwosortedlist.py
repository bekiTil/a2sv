class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode()
        news=new
        while list1 and list2:
            if list1.val>=list2.val:
                
                news.next=list2
                list2=list2.next
            else:
                
                news.next=list1
                list1=list1.next
            news=news.next
        if list1==None:
            news.next=list2
        else:
            news.next=list1
        return new.next
            
                
        
