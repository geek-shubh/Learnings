#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/running-sum-of-1d-array/
# Runtime: 28 ms, faster than 52.84% of Python online submissions for Running Sum of 1d Array.
# Memory Usage: 13.7 MB, less than 10.73% of Python online submissions for Running Sum of 1d Array.


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums