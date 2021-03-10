"""
Question: Average of Levels in Binary Tree
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        count = []
        
        def getLevelSum(node, level):
            if len(res) <= level:
                res.append(node.val)
                count.append(1).
            else:
                res[level] += node.val
                count[level] += 1
            if node.left:
                getLevelSum(node.left, level+1)
            if node.right:
                getLevelSum(node.right, level+1)
                
        getLevelSum(root, 0)
        return [s/c for s, c in zip(res, count)]