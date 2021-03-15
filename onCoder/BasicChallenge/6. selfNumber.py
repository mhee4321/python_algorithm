class Solution:
    def solution(self, a):
        self.a = a
        self.sum = 0
        self.res = []

        for i in range(1, self.a + 1):
            self.sum = i
            for j in range(0, len(str(i))):
                self.sum += int(str(i)[j])

            self.res.append(str(self.sum))
        return self.res.count(str(a))

