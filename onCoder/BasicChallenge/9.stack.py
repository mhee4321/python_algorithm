class Solution:
    def solution(self, cmds):
        self.c = cmds
        self.s = []
        for i in self.c:
            if "PUSH" in i:
                d=i[5:]
                self.s.append(int(d))
            if "POP" in i and self.s !=[]:
                self.s.pop()
        return self.s


