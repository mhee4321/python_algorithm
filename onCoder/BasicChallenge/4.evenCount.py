class Solution:
    def solution(self, arr):
        cnt=0
        for i in range(len(arr)):
            if arr[i] % 2 ==0:
                cnt += 1
        return cnt