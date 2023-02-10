# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def level(node):
            return max(level(node.left), level(node.right)) + 1 if node else 0
        
        def dfs(node, height):
            return 0 if not node else dfs(node.left, height-1) + dfs(node.right, height-1) if height else node.val
        
        return dfs(root, level(root)-1)