# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        def getTotal(head):
            if not head:
                return
            nonlocal total
            total+=head.val
            getTotal(head.left)
            getTotal(head.right)
        getTotal(root)
        def makegst(head):
            if not head:
                return
            nonlocal total
            makegst(head.left)
            temp = head.val
            head.val = total 
            total-=temp
            makegst(head.right)
        makegst(root)
        return root

            

        