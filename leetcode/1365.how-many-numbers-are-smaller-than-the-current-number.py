#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Runtime: 624 ms, faster than 5.01% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.6 MB, less than 31.69% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out_arr = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    cnt += 1
            out_arr.append(cnt)
        return out_arr