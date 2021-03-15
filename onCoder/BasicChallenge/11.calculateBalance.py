class Solution:
    def solution(self, balance, transactions):
        self.b = balance
        self.t = transactions
        for i in self.t:
            if "C" in i:
                a=i[2:]
                self.b += int(a)
            if "D" in i:
                a=i[2:]
                self.b -= int(a)
        return self.b

