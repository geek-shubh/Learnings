#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/add-two-numbers/
# Runtime: 48 ms, faster than 97.95% of Python online submissions for Add Two Numbers.
# Memory Usage: 13.6 MB, less than 38.70% of Python online submissions for Add Two Numbers.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r_node = None
        head = None
        carry = 0

        while l1 or l2:
            if l1 and l2:
                sum = carry + l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = carry + l1.val
                l1 = l1.next
            else:
                sum = carry + l2.val
                l2 = l2.next

            carry = sum / 10
            sum = sum % 10

            if r_node is None:
                r_node = ListNode(sum)
                head = r_node
            else:
                r_node.next = ListNode(sum)
                r_node = r_node.next
        if carry:
            r_node.next = ListNode(carry)
        return head
