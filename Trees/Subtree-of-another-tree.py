# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Trees.basic import TreeNode


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return False
        
        def SameTree(root1:TreeNode,root2:TreeNode):
            if root1 is None and root2 is None:
              return True
            if root1 is None or root2 is None:
              return False
            if root1.val!=root2.val:
                return False
            return (
             SameTree(root1.left, root2.left)
             and
             SameTree(root1.right, root2.right)
              )
        return (
          SameTree(root, subRoot)
          or
          self.isSubtree(root.left, subRoot)
          or
          self.isSubtree(root.right, subRoot)
          )