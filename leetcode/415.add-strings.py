#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/add-strings/
# Runtime: 48 ms, faster than 10.14% of Python online submissions for Add Strings.
# Memory Usage: 13.6 MB, less than 68.84% of Python online submissions for Add Strings.


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))