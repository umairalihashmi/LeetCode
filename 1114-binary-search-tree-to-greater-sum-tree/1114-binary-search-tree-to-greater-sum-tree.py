# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def getTotal(head,total):
            if not head:
                return total
            total = getTotal(head.left,total+head.val)
            total = getTotal(head.right,total)
            return total

        def makegst(head,total):
            if not head:
                return total
            total = makegst(head.left,total)
            temp = head.val
            head.val = total 
            total = makegst(head.right,total-temp)
            return total
        
        makegst(root,getTotal(root,0))
        return root

            

        