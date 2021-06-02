#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/add-digits/
# Runtime: 16 ms, faster than 87.74% of Python online submissions for Add Digits.
# Memory Usage: 13.7 MB, less than 6.93% of Python online submissions for Add Digits.


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        while 1:
            d = 0
            while num:
                d = d + (num % 10)
                num /= 10
            if d < 10:
                return d
            num = d

        return num