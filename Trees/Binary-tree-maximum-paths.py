from Trees.basic import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        result = [float('-inf')]

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current_path = left + node.val + right

            result[0] = max(result[0], current_path)

            return node.val + max(left, right)

        dfs(root)

        return result[0]