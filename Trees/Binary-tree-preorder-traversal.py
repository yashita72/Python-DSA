# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Trees.basic import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer=[]
        def preorder(root):
          if root is None:
            return
        
          answer.append(root.val)
          preorder(root.left)
          preorder(root.right)
        preorder(root)
        return answer



        