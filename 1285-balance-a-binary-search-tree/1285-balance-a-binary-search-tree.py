# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def trav(root):
            if not root:
                return 
            trav(root.left)
            arr.append(root.val)
            trav(root.right)

        def construct(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            return TreeNode(arr[len(arr)//2],construct(arr[:(len(arr)//2)]),construct(arr[(len(arr)//2)+1:]))

        trav(root)
        return construct(arr)