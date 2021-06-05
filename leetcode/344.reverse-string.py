#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/reverse-string/
# Runtime: 160 ms, faster than 89.67% of Python online submissions for Reverse String.
# Memory Usage: 21.1 MB, less than 54.67% of Python online submissions for Reverse String.


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s

        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

        return s