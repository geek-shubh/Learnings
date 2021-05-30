#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Runtime: 88 ms, faster than 25.08% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13.8 MB, less than 22.35% of Python online submissions for Median of Two Sorted Arrays.


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        num3 = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                num3.append(nums1[i])
                i += 1
            else:
                num3.append(nums2[j])
                j += 1
        while i < len(nums1):
            num3.append(nums1[i])
            i += 1
        while j < len(nums2):
            num3.append(nums2[j])
            j += 1
        len_num3 = len(num3)
        mid_len = len_num3 / 2
        if len_num3 % 2 == 1:
            return float(num3[mid_len])
        else:
            return float(float(num3[mid_len] + num3[mid_len - 1]) / 2)

