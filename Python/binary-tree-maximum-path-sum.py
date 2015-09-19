# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find the maximum path sum.
# 
# The path may start and end at any node in the tree.
# 
# For example:
# Given the below binary tree,
# 
#        1
#       / \
#      2   3
#     / \
#    4   5                                                                                                                        
# Return 6.
#
# 求从一点到另一点最大距离

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    maxSum = float("-inf")

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxPathSumRecu(root)
        return self.maxSum
    
    def maxPathSumRecu(self, root):

        if root is None:
            return 0
        # 根节点＋左子树＋右子树　
        left = max(0, self.maxPathSumRecu(root.left))
        right = max(0, self.maxPathSumRecu(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        return root.val + max(left, right)
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    result = Solution().maxPathSum(root)
    print result
