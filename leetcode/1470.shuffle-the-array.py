#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/shuffle-the-array/
# Runtime: 52 ms, faster than 14.81% of Python online submissions for Shuffle the Array.
# Memory Usage: 13.8 MB, less than 5.14% of Python online submissions for Shuffle the Array.


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        out_arr = []
        i = 0
        while i < n :
            out_arr.append(nums[i])
            out_arr.append(nums[i+n])
            i += 1
        return out_arr