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
        trav(root)
        # print(arr)
        # print(arr[len(arr)//2])
    
        def construct(arr):
            print("array:",arr)
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
                
            node = TreeNode(arr[len(arr)//2])
            # print("new node made:",node)
            node.left = construct(arr[:(len(arr)//2)])
            node.right = construct(arr[(len(arr)//2)+1:])

            return node
        
        # construct(arr) 

        return construct(arr)