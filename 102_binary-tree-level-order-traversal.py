# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        """ 深度优先递归法 """
        def helper(node, level):
            if level == len(levels):
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level+1)

        levels = []
        if not root: return levels
        helper(root, 0)
        return levels

    def levelOrder1(self, root: TreeNode):
        """ 广度优先迭代法 """
        levels = []
        if not root: return levels

        level = 0
        queue = [root]

        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.pop(0)
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels
