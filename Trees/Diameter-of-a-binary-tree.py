# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Trees.basic import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=0
        def height(node):
          nonlocal max_diameter
          if node is  None: return 0
          left_height=height(node.left)
          right_height=height(node.right) 
          curr_diameter=left_height+right_height
          max_diameter=max(curr_diameter,max_diameter)
          heights=1+max(left_height,right_height)
          return heights
        height(root)
        return max_diameter