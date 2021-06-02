#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/binary-tree-right-side-view/
# Runtime: 44 ms, faster than 5.53% of Python online submissions for Binary Tree Right Side View.
# Memory Usage: 13.4 MB, less than 50.36% of Python online submissions for Binary Tree Right Side View.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        l_tree = self.rightSideView(root.left)
        r_tree = self.rightSideView(root.right)
        if len(r_tree) < len(l_tree):
            return [root.val] + r_tree + l_tree[len(r_tree):]
        return [root.val] + r_tree
