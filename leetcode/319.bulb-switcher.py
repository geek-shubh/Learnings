#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/bulb-switcher/
# Runtime: 40 ms, faster than 7.69% of Python online submissions for Bulb Switcher.
# Memory Usage: 13.3 MB, less than 60.00% of Python online submissions for Bulb Switcher.

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (int(n**0.5))