#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/merge-k-sorted-lists/

# Runtime: 72 ms, faster than 99.46% of Python online submissions for Merge k Sorted Lists.
# Memory Usage: 22.1 MB, less than 35.53% of Python online submissions for Merge k Sorted Lists.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = []
        for head in lists:
            while head:
                vals.append(head.val)
                head = head.next

        vals.sort()

        if vals == []:
            return None

        else:
            head = ListNode(vals[0])
            temp = head
            for i in range(1, len(vals)):
                temp.next = ListNode(vals[i])
                temp = temp.next
        return head
