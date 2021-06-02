#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/richest-customer-wealth/
# Runtime: 36 ms, faster than 78.83% of Python online submissions for Richest Customer Wealth.
# Memory Usage: 13.5 MB, less than 47.55% of Python online submissions for Richest Customer Wealth.


class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_w = 0
        for i in range(len(accounts)):
            t_w = 0
            for j in range(len(accounts[i])):
                t_w += accounts[i][j]
            max_w = max(max_w, t_w)
        return max_w
