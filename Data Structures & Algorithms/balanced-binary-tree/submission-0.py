# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxD = 0
        
        def dfs(root):
            nonlocal maxD
            if not root:
                return 0

            dl = dfs(root.left)
            dr = dfs(root.right)

            maxD = max(maxD, abs(dl - dr))

            return 1 + max(dl, dr)

        dfs(root)
        return maxD <= 1