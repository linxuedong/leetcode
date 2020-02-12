# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """ 
        中序遍历，按照升序排序，且元素不重复
        """
        in_order = self.inOrder(root)
        
        return in_order == sorted(list(set(in_order)))


    def inOrder(self, root: TreeNode):
        if root:
            return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        else:
            return []


    def isValidBST2(self, root: TreeNode) -> bool:
        """ 递归 """
        return  self.helper(root)

    def helper(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
        # 节点为空
        if root is None:
            return True

        val = root.val
        if val <= lower or val >= upper:
            return False
        
        # 左子树
        if not self.helper(root.left, lower, val):
            return False

        # 右子树
        if not self.helper(root.right, val, upper):
            return  False
        return True
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    t = TreeNode(2)
    t.left = TreeNode(1)
    t.right = TreeNode(3)

    Solution().isValidBST(t)
    print(Solution().isValidBST(None))