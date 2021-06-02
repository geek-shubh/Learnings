#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/add-binary/
# Runtime: 16 ms, faster than 92.65% of Python online submissions for Add Binary.
# Memory Usage: 13.4 MB, less than 94.32% of Python online submissions for Add Binary.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2) + int(b,2)))[2:]