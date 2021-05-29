#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/multiply-strings/submissions/
# Runtime: 24 ms, faster than 67.60% of Python online submissions for Multiply Strings.
# Memory Usage: 13.4 MB, less than 95.83% of Python online submissions for Multiply Strings.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)*int(num2))