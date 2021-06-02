#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Runtime: 20 ms, faster than 42.53% of Python online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.4 MB, less than 65.95% of Python online submissions for Number of Steps to Reduce a Number to Zero.

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 2:
            return num
        cnt = 0
        while num:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            cnt += 1
        return cnt