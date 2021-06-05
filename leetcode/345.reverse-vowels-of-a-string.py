#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Runtime: 56 ms, faster than 61.82% of Python online submissions for Reverse Vowels of a String.
# Memory Usage: 15.5 MB, less than 55.24% of Python online submissions for Reverse Vowels of a String.


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        v_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in v_list:
                while j > i:
                    if s[j] in v_list:
                        # print s[i], s[j], i, j
                        s[i], s[j] = s[j], s[i]
                        j -= 1
                        break
                    j -= 1
            i += 1
        return str("".join(s))


if __name__ == '__main__':
    sol = Solution()
    print sol.reverseVowels("hello shubham !")
