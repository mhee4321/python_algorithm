class Solution:
    def solution(self, stats):
        self.s = stats
        self.t=[]
        for i in self.s:
            one=0
            two=0
            for j in i:
                if j == "1":
                    one+=1
                if j == "2":
                    two+=1
            res = one/(one+two)
            self.t.append(res)
        m = self.t.index(min(self.t))
        return m
