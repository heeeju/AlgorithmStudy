n = int(input())
nums = list(map(int, input().split()))
new_nums = []
m = max(nums)

for num in nums:
  new_nums.append(num/m*100)

print(sum(new_nums)/len(new_nums))
