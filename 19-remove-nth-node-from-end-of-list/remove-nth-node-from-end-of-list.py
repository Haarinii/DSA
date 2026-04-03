# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next= head
        temp = dummy
        for i in range(n):
            temp=temp.next
        ptr= dummy
        while temp.next != None:
            ptr=ptr.next
            temp=temp.next
        ptr.next= ptr.next.next
        return dummy.next
        