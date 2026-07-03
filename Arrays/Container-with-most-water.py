class Solution:
    def maxArea(self, height: list[int]) -> int:
       left, right = 0, len(height) - 1
       max_area=(min(height[left],height[right])*(right-left))
       while left<right:
           area = (min(height[left],height[right])*(right-left))
           if area>max_area:
                max_area=area
           if(height[left]<height[right]):
              left+=1
           else:
                right-=1
       return max_area
        #time complexity is big oh of n and space is constant
        #brute forcee to do loops lga dete to n sqaure hojati