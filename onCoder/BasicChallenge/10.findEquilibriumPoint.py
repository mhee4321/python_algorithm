from math import *


class Solution:
    def solution(self, x1, m1, x2, m2):
        self.x1 = x1
        self.m1 = m1
        self.x2 = x2
        self.m2 = m2

        # 만유인력의 법칙 =  질량1*질량2/거리^2
        res = ((sqrt(self.m1) * self.x2) + (sqrt(self.m2) * self.x1)) / (sqrt(self.m2) + sqrt(self.m1))
        return res

