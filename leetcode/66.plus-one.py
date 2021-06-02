# https://leetcode.com/problems/plus-one/
# Runtime: 48 ms, faster than 32.79% of Python online submissions for Plus One.
# Memory Usage: 13.5 MB, less than 12.47% of Python online submissions for Plus One.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(str(int("".join(map(str, digits))) + 1))
