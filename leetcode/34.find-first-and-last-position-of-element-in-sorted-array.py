#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ Runtime: 64 ms, faster than
# 75.66% of Python online submissions for Find First and Last Position of Element in Sorted Array. Memory Usage: 14.5
# MB, less than 88.19% of Python online submissions for Find First and Last Position of Element in Sorted Array.


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                i = mid - 1
                j = mid + 1
                while i >= 0:
                    if nums[mid] != nums[i]:
                        break
                    i -= 1
                while j <= len(nums) - 1:
                    if nums[mid] != nums[j]:
                        break
                    j += 1
                return [min(mid, i + 1), max(mid, j - 1)]
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]
