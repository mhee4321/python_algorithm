class Solution:
    def solution(self, arr):
        self.a = arr
        self.t = []
        for i in self.a:
            self.t.append(str(i))
        self.t.sort()
        # ['143', '15', '167']

        return list(map(int, self.t))

a = Solution()
s = [15,143,167]
Solution.solution(a, s)