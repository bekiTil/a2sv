 def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new=[]
        while head!=None:
            new.append(head.val)
            head=head.next
        news=list(reversed(new))
        print(new)
        print(news)
        for i in range(len(news)):
            if new[i]!=news[i]:
                return False
        return True
