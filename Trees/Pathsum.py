class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, curr_sum):

            # Base case: empty node
            if node is None:
                return False

            # Add current node's value
            curr_sum += node.val

            # Base case: leaf node
            if node.left is None and node.right is None:
                return curr_sum == targetSum

            # Recursive case: left OR right
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

        return dfs(root, 0)