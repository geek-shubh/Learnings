#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/jewels-and-stones/
# Runtime: 32 ms, faster than 24.04% of Python online submissions for Jewels and Stones.
# Memory Usage: 13.5 MB, less than 26.10% of Python online submissions for Jewels and Stones.


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        cnt = 0
        for s in stones:
            if s in jewels:
                cnt += 1
        return cnt

