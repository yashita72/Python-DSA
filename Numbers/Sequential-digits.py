class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        strs='123456789'
        result=[]
        for le in range(len(str(low)),len(str(high))+1):
            left,right=0,le
            while(right<=9):
                window=strs[left:right]
                if int(window) >= low and int(window) <= high:
                    result.append(int(window))
                left+=1
                right+=1
        return result