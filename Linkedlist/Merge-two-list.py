# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        curr=list3
        head1=list1
        head2=list2
        while head1 is not None and head2 is not None:
            if head1.val<head2.val:
                curr.next=head1
                head1=head1.next
            else:
                curr.next=head2
                head2=head2.next
            
            curr = curr.next 
        if head1:
                curr.next=head1
        if head2:
                curr.next=head2
        return list3.next
            
        