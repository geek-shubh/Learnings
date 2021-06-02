#!/usr/bin/env python
__author__ = "geek-shubh"

# https://leetcode.com/problems/design-parking-system/
# Runtime: 144 ms, faster than 10.31% of Python online submissions for Design Parking System.
# Memory Usage: 14.1 MB, less than 9.53% of Python online submissions for Design Parking System.


class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big:
                self.big -= 1
                return True
            return False
        elif carType == 2:
            if self.medium:
                self.medium -= 1
                return True
            return False
        else:
            if self.small:
                self.small -= 1
                return True
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
