# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(-1)
        curr=dummy
        temp1=l1
        temp2=l2
        carry=0
        while temp1 is not None or temp2 is not None:
            total =carry
            if temp1:
                total+= temp1.val
            if temp2:
                total+=temp2.val
            new_node=ListNode(total%10)
            carry=total//10
            curr.next= new_node
            curr=curr.next
            if temp1:
                temp1=temp1.next
            if temp2:
                temp2=temp2.next
        if carry:
            curr.next=ListNode(carry)
        return dummy.next