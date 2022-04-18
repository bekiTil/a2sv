def has_cycle(head):
    slow=head 
    fast=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if (slow==fast):
            return 1
    return 0
