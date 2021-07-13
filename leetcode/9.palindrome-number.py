#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/palindrome-number/
# Runtime: 60 ms, faster than 47.81% of Python online submissions for Palindrome Number.
# Memory Usage: 13.3 MB, less than 88.92% of Python online submissions for Palindrome Number.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return False if x < 0 else str(x) == str(x)[::-1]