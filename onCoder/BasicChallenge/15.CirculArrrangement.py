class Solution:
    def solution(self, n1, n2, K):
        self.n1 = n1
        self.n2 = n2
        self.K = K
        self.t = []

        if self.n2 >= 1 and self.n1 >= 1:
            for i in range(self.n1 + self.n2):
                self.t.append('M')
            d = self.K
            i = 0
            r = []
            while True:
                if d > len(self.t):
                    while True:
                        d = d - len(self.t)
                        if d <= len(self.t):
                            break
                self.t.remove(self.t[d - 1])
                r.append(d - 1)
                d = d - 1 + self.K
                i += 1
                if i == self.n2:
                    break
            r = reversed(r)
            for i in r:
                self.t.insert(i, 'F')
        else:
            for i in range(self.n2):
                self.t.append('F')
            for i in range(self.n1):
                self.t.append('M')
        self.t = "".join(self.t)
        return self.t

