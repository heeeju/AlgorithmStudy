import math

def solution(nums):
    answer = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range (j+1, len(nums)):
                num = nums[i]+nums[j]+nums[k]
                check = 0
                for x in range(2, int(math.sqrt(num))+1):
                    if num % x == 0:
                        check = 1
                        break
                if check == 0:
                    answer +=1
    return answer
