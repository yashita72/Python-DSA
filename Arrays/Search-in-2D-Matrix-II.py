class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
       
       row=0
       col=len(matrix[0])-1
       while row < len(matrix) and col >= 0:
         value=matrix[row][col]
         if value==target:
           return True
         elif value>target:
                col=col-1
         else :
                row=row+1
       return False         

   