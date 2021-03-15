from math import *


class Solution:
    def solution(self, x, y1, y2):
        self.a = x
        self.b = y1
        self.c = y2

        sum = 0
        for i in range(len(self.a)):
            if (self.b[i] > self.c[i]):
                arg1 = self.b[i]
                arg2 = self.c[i]
            else:
                arg1 = self.c[i]
                arg2 = self.b[i]
            res = atan2(arg1, self.a[i]) / pi
            res -= atan2(arg2, self.a[i]) / pi
            sum += res
        return sum

