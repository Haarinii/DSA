# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(left, right):
            dummy=ListNode(-1)
            res=dummy
            while left and right:
                if left.val<right.val:
                    res.next=left
                    left=left.next
                else:
                    res.next=right
                    right=right.next
                res=res.next
            if right:
                res.next=right
            else:
                res.next=left
            return dummy.next

        def findMid(head):
            if not head or not head.next:
                return head
            slow=head
            fast= head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow

        def mergesort(head):
            if not head or not head.next:
                return head
            mid=findMid(head)
            right=mid.next
            mid.next=None
            left=head
            left=mergesort(left)
            right=mergesort(right)
            return merge(left, right)
        return mergesort(head)
        

        