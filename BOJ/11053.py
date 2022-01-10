n = int(input())
nums = list(map(int, input().split()))

nums = [0] + nums
length = [0]
info = [0]

for i in range(1, len(nums)):
  idx = 0
  for j in range(len(info)-1, -1, -1):
    if nums[i] > info[j]:
      if j+1 == len(info):
        info.append(nums[i])
      else:
        info[j+1] = nums[i]
      idx = j+1
      break
  length.append(idx)

print(max(length))
