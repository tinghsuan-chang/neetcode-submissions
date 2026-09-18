# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # identify midpoint of list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # "slow" is the 2nd half of list
        
        # reverse 2nd half of list
        curr, prev = slow, None
        while curr:
            child = curr.next
            curr.next = prev
            prev = curr
            curr = child
        l2 = prev 
        print(l2.val)

        # combine 1st half and the reversed 2nd half
        l1 = head
        cur, nex = l1, l2
        while cur and (cur != nex):
            child = cur.next
            cur.next = nex
            cur = nex
            nex = child
        
        
    