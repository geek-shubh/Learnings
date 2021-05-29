#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/two-sum/submissions/
# Runtime: 708 ms, faster than 10.16% of Python online submissions for Two Sum.
# Memory Usage: 14.1 MB, less than 21.34% of Python online submissions for Two Sum.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {}
        for i in range(len(nums)):
            if nums[i] in temp_dict.keys():
                return temp_dict[nums[i]], i
            else:
                temp_dict[target-nums[i]] = i
