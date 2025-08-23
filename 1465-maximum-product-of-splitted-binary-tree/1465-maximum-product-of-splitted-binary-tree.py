# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        prodandtotal = [0,0]
        def dfs1(root):
            if not root: return
            prodandtotal[1] += root.val
            dfs1(root.left)
            dfs1(root.right)
        def dfs2(root):
            if not root: return 0
            sum_till_node = root.val + dfs2(root.left) + dfs2(root.right)
            prod = (prodandtotal[1]- sum_till_node)*sum_till_node 
            if prod > prodandtotal[0]: prodandtotal[0] = prod
            return sum_till_node
        dfs1(root)
        dfs2(root)    
        return prodandtotal[0]%(10**9 + 7)
        