class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        count_odd,count_even=0,0
        for i in nums1:
            if i%2 == 0:
                count_even+=1
            else:
                count_odd+=1
        if count_odd == len(nums1)-1 or count_even == len(nums1)-1 or (count_odd > 1 and count_even > 1) or count_odd == 0 or count_odd >= 2:
            return True
        return False