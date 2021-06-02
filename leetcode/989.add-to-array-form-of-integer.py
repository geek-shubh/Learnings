#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/add-to-array-form-of-integer/
# Runtime: 392 ms, faster than 21.83% of Python online submissions for Add to Array-Form of Integer.
# Memory Usage: 14 MB, less than 53.30% of Python online submissions for Add to Array-Form of Integer.


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        return list(str(int("".join(map(str, num))) + k))
