cnt = int(input())
nums = sorted(map(int, input().split()))

if len(nums) % 2 == 0:
  n = nums[0] * nums[len(nums)-1]
else:
  n = nums[len(nums)//2]**2

print(n)
