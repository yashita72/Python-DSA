# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Trees.basic import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        answer=[]
        path=[]
        if root is None:
            return []
        def dfs(root,path):
            if root is None:
                return 
            path.append(root.val)
            if root.left==None and root.right==None:
                answer.append("->".join(map(str, path)))
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()
        dfs(root, path)
        return answer
                
        