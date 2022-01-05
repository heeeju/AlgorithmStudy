nums = [int(input()) for i in range(int(input()))]

#bubble sort
length = len(nums)-1
for i in range(length):
  for j in range(length-i):
    if nums[j] > nums[j+1]:
      nums[j], nums[j+1] = nums[j+1], nums[j]

print('\n'.join(map(str, nums)))
