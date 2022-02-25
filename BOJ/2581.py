import math
m = int(input())
n = int(input())
nums=[]

for i in range(m, n+1):
  if i==1:
    continue
  elif i==2:
    nums.append(2)
    continue
  check = 0
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      check = 1
      break
  if check==0:
    nums.append(i)

if len(nums)==0:
  print(-1)
else:
  print(sum(nums))
  print(nums[0])
