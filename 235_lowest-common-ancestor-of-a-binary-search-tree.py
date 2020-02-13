# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ 
        二叉搜索树中左子树小于根节点，右子树大于根节点，
        所以可以根据节点的值来判断公共祖先
        """
        # 根为空或一个节点等于根
        if not root or root == p or root == q:
            return root
        
        # p q 节点的值都小于根节点
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p q 节点的值都大于根节点
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root