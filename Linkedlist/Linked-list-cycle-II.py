# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
     
     slow, fast = head, head
     has_cycle = False
    
     # Phase 1: cycle exist karta hai kya, meeting point dhoondo
     while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
     
     if not has_cycle:
        return None  # cycle nahi hai, fast None tak pahunch gaya
    
     # Phase 2: ek pointer head se, ek meeting point se, same speed
     ptr1 = head
     ptr2 = slow
     while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
     return ptr1   # yahi cycle ka start hai   