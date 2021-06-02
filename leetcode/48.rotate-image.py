#!/usr/bin/env python
__author__ = "geek-shubh"


# https://leetcode.com/problems/rotate-image/
# Runtime: 44 ms, faster than 5.17% of Python online submissions for Rotate Image.
# Memory Usage: 13.5 MB, less than 38.75% of Python online submissions for Rotate Image.


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix[0])):
            matrix[i].reverse()

        return matrix
