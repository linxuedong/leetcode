# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if not node: return 

            if L <= node.val <= R:
                self.result += node.val

            children = [node.left, node.right]
            for c in children:
                dfs(c)

        self.result = 0
        dfs(root)
        return self.result