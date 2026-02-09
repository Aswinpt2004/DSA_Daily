# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            visited.append(node.val)
            inorder(node.right)

        inorder(root)

        def construct_tree( left , right):
            if left > right:
                return None 

            mid = (left + right )//2 
            left_node = construct_tree(left, mid - 1)
            right_node =  construct_tree(mid + 1, right)

            return TreeNode(visited[mid], left_node, right_node)
       
        N = len(visited)
        return construct_tree(0,N-1)