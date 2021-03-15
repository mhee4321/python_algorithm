class Solution:
    def solution(self, a):
        cnt=0
        for i in range(1, a+1):
            if '13' in str(i):
                cnt+=1
        return cnt