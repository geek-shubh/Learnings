#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/range-sum-of-bst/
# Runtime: 420 ms, faster than 5.08% of Python online submissions for Range Sum of BST.
# Memory Usage: 29.6 MB, less than 90.53% of Python online submissions for Range Sum of BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root:
            self.rangeSumBST(root.left, low, high)
            if low <= root.val <= high:
                self.sum += root.val
            self.rangeSumBST(root.right, low, high)
        return self.sum
