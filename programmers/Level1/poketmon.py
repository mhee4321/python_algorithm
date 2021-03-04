def solution(nums):
    result = set()
    for i in nums:
        result.add(i)
    if len(result)> len(nums)/2:
        return len(nums)//2
    else:
        return len(result)

def solution2(nums):
    return min(len(set(nums)), len(nums)//2)

nums = [3,1,2,3]
print(solution(nums))