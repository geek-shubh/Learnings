#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/single-number/
# Runtime: 104 ms, faster than 86.16% of Python online submissions for Single Number.
# Memory Usage: 15.4 MB, less than 92.77% of Python online submissions for Single Number.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

