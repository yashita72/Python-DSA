# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Trees.basic import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer=[]
        def inorder(root):
          if root is None:
            return
          inorder(root.left)
          answer.append(root.val)
          inorder(root.right)
        inorder(root)
        return answer