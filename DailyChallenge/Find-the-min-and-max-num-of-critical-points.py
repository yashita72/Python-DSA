# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        def get_length(head):
            count = 0
            current = head
            while current is not None:
                count += 1
                current = current.next
            return count
        Len=get_length(head)
        if Len<=2:
            return [-1,-1]
        prev=head.val
        temp=head.next
        D=[]
        for i in range(1,Len-1):
            if (temp.val > prev and temp.val > temp.next.val) or  (temp.val < prev and temp.val < temp.next.val):
                D.append(i)
            prev=temp.val
            temp=temp.next
        if len(D) < 2:
            return [-1, -1]

        min_dist = min(D[i+1] - D[i] for i in range(len(D)-1))
        max_dist = D[-1] - D[0]
        return [min_dist, max_dist]