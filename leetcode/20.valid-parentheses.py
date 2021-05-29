#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/valid-parentheses/
# Runtime: 12 ms, faster than 97.86% of Python online submissions for Valid Parentheses.
# Memory Usage: 13.7 MB, less than 31.84% of Python online submissions for Valid Parentheses.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        inv_p_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        # check for odd length string
        if len(s) % 2 == 1:
            return False

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if len(stack) > 0:
                    curr_close = stack.pop()
                    if not inv_p_dict[i] == curr_close:
                        return False
                else:
                    return False

        if len(stack) > 0:
            return False
        return True
