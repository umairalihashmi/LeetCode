# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(head):
            if not head:
                return
            if not (head.left or head.right):
                if head.val == target:
                    head.val = -1
                return
            dfs(head.left)
            dfs(head.right)
            if  head.left  and head.left.val == -1:
                head.left = None
            if  head.right  and head.right.val == -1:
                head.right = None
            if not (head.left or head.right) and head.val == target:
                head.val = -1
        dfs(root)
        if root.val == -1:
            return None
        return root