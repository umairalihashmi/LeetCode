# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not (root1 or root2):
            return True
        if not ( root1 and root2):
            return False

        def get_val(root):
            if not root:
                return 0
            return root.val

        def mod_tree(root):
            if not root:
                return
            a = get_val(root.left)
            b = get_val(root.right)
            if a < b:
                pass
            else:
                root.left,root.right = root.right,root.left
            mod_tree(root.left)
            mod_tree(root.right)
        mod_tree(root1)
        mod_tree(root2)
        def isIdentical(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            return (r1.val == r2.val and
                    isIdentical(r1.left, r2.left) and
                    isIdentical(r1.right, r2.right))

        return isIdentical(root1,root2)
        
        