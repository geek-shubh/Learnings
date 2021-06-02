#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/roman-to-integer/
# Runtime: 92 ms, faster than 5.06% of Python online submissions for Roman to Integer.
# Memory Usage: 13.5 MB, less than 26.78% of Python online submissions for Roman to Integer.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        r_int = 0
        i = 0
        l = len(s)
        while i < l:
            if s[i:i + 2] in roman_dict:
                r_int += roman_dict[s[i:i + 2]]
                i += 2
            else:
                r_int += roman_dict[s[i:i + 1]]
                i += 1
        return r_int


