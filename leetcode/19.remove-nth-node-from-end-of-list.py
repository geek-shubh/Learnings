#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Runtime: 16 ms, faster than 92.04% of Python online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.4 MB, less than 69.43% of Python online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_node = ListNode(None, head)
        prev = fast = dummy_node
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy_node.next

