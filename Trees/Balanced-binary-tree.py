class Solution:
    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftheight = self.height(root.left)
        rightheight = self.height(root.right)

        return (
            abs(leftheight - rightheight) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )