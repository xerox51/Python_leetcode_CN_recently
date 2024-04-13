# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.node = TreeNode()
        def preOrder(root,target):
            if root is None:
                return
            if root.val == target:
                self.node = root
                return
            preOrder(root.left,target)
            preOrder(root.right,target)
    
        if original is None:
            return None
        if cloned is None:
            return original
        preOrder(cloned,target.val)
        return self.node
        