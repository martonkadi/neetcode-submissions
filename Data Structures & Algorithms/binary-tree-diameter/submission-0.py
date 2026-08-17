# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        
        def dfs(root):
            nonlocal d
            if not root:
                return 0

            dl = dfs(root.left)
            dr = dfs(root.right)

            d = max(d, dl + dr)

            return 1 + max(dl, dr)

        dfs(root)
        return d