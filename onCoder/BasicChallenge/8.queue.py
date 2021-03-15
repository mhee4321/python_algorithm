class Solution:
    def solution(self, cmds):
        self.c = cmds
        self.q = []
        for i in self.c:
            if "PUSH" in i:
                d=i[5:]
                self.q.append(int(d))
            if "POP" in i and self.q!=[]:
                self.q.pop(0)
        return self.q

