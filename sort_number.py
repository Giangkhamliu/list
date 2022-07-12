def solution(nums):
    if nums!=[] and nums!=None:
        nums.sort()
        return nums
    else:
        return []
print(solution([1,5,3,8,6,5]))
print(solution([]))
print(solution([10,0,9,5,34]))
print(solution(None))