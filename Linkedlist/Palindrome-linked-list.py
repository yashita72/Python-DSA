# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        left=0
        right=len(vals)-1
        while left<right:
            if vals[left] != vals[right]:
               return False
            left+=1
            right-=1
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left, right = head, prev
        while right:  # right half is shorter or equal
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
        