#!/usr/bin/env python
__author__ = "geek-shubh"


class Node(object):
    # constructor to initialize the node object
    def __init__(self, val):
        self.data = val
        self.next = None


class link_list(object):

    # constructor to initialize root of link list
    def __init__(self):
        self.root = None

    # function to insert a node in link list at the end
    def insert_node(self, val):

        # if root is None insert first value to root
        if self.root is None:
            self.root = Node(val)
            return
        else:
            temp_node = self.root
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = Node(val)

    # function to reverse a linked list
    def reverse_list(self):
        prev_node = None
        curr_node = self.root
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.root = prev_node

    # function to sort a list
    def sort_list(self):
        i_node = self.root
        while i_node:
            j_node = i_node.next
            while j_node:
                if i_node.data > j_node.data:
                    i_node.data, j_node.data = j_node.data, i_node.data
                j_node = j_node.next
            i_node = i_node.next

    # function to find a loop in link list
    def find_loop(self):
        slow_p = self.root
        fast_p = self.root
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

    # function to print a list
    def print_list(self):
        temp_n = self.root
        while temp_n:
            print(temp_n.data)
            temp_n = temp_n.next

    # function to check palindrome
    def check_palindrome(self):
        stack = []
        t_node = self.root

        while t_node:
            stack.append(t_node.val)
            t_node = t_node.next

        t_node = self.root
        while t_node:
            t = stack.pop()
            if t != t_node.val:
                return False
            t_node = t_node.next

        return True


if __name__ == '__main__':
    l_list = link_list()
    l_list.insert_node(10)
    l_list.insert_node(6)
    l_list.insert_node(12)
    l_list.insert_node(10)

    print("Link List")
    print(l_list.print_list())
    print

    print("Sorted Link List")
    l_list.sort_list()
    print(l_list.print_list())
    print

    print("Reverse Link List")
    l_list.reverse_list()
    print(l_list.print_list())
    print

    print("Check Palindrome")
    print(l_list.check_palindrome())
    print
