#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/defanging-an-ip-address

# Runtime: 44 ms, faster than 5.08% of Python online submissions for Defanging an IP Address.
# Memory Usage: 13.8 MB, less than 6.92% of Python online submissions for Defanging an IP Address.

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")


# Runtime: 28 ms, faster than 5.08% of Python online submissions for Defanging an IP Address.
# Memory Usage: 13.5 MB, less than 58.12% of Python online submissions for Defanging an IP Address.

class Solution2(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return "[.]".join(address.split("."))
