class Solution:
    def solution(self, sequence):
        self.s = sequence
        self.t = list(set(self.s))

        for i in self.t:
            k = self.s.count(i)
            for j in range(k - 1):
                self.s.remove(i)

        return self.s

