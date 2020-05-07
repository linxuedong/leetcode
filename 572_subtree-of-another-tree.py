# 572. 另一个树的子树
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

# 示例 1:
# 给定的树 s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 t：
#    4 
#   / \
#  1   2
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

# 示例 2:
# 给定的树 s：
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# 给定的树 t：
#    4
#   / \
#  1   2
# 返回 false。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subtree-of-another-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isSameTree(s, t):
            return True
        sub_trees = []
        if s.left:
            sub_trees.append(s.left)
        if s.right:
            sub_trees.append(s.right)

        for sub_tree in sub_trees:
            if self.isSameTree(sub_tree, t):
                return True
            if self.isSubtree(sub_tree, t):
                return True
        return False

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        # 都为 None
        if s is None and t is None:
            return True

        # 一边不为 None
        if s is None and t is not None:
            return False
        if s is not None and t is None:
            return False
        # 都不为 None
        if s.val != t.val:
            return False
        else:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)