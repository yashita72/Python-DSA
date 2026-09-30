# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Trees.basic import TreeNode


class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        lefdep=self.minDepth(root.left)
        righdep=self.minDepth(root.right)
        if lefdep==0:
            return righdep+1
        if righdep==0:
            return lefdep+1
        return min(lefdep, righdep) + 1
        