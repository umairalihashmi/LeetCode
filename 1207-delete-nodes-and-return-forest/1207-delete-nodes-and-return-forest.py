# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        delete = set(to_delete)
        def trav(head):
            if not head:
                return False
            if head.val in delete:
                if head.left:
                    if head.left.val not in delete:
                        ans.append(head.left)
                    if trav(head.left):
                        head.left = None
                if head.right:
                    if head.right.val not in delete:
                        ans.append(head.right)
                    if trav(head.right):
                        head.right = None
                return True 
            else:
                if trav(head.left):
                    head.left = None
                if trav(head.right):
                    head.right = None
            return False
        trav(root)
        if root.val not in delete:
            ans.append(root)
        return ans
