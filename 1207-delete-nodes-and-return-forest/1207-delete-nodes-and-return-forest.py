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
                print("leaf")
                return False
            if head.val in delete:
                print(head.val,"in delete")
                if head.left:
                    if head.left.val not in delete:
                        ans.append(head.left)
                    print("sending below left from",head.val)
                    if trav(head.left):
                        head.left = None
                if head.right:
                    if head.right.val not in delete:
                        ans.append(head.right)
                    print("sending below right from",head.val)
                    if trav(head.right):
                        head.right = None
                return True 
            else:
                print("sending below left from non delete",head.val)
                if trav(head.left):
                    print(head.left.val,"in delete")
                    head.left = None
                print("sending below right from non delete",head.val)
                if trav(head.right):
                    print(head.right.val,"in delete")
                    head.right = None
            return False
        trav(root)
        if root.val not in delete:
            ans.append(root)

        return ans
