def fibonacci(n):
  global fib_num
  if n==0:
    return 0
  elif n==1:
    fib_num[n]=1
    return 1

  if fib_num[n] != 0:
    return fib_num[n]
  else:
    fib_num[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_num[n]

T = int(input())
nums = [int(input()) for i in range(T)]
fib_num = [0 for i in range(max(nums)+1)]
fibonacci(max(nums))

for n in nums:
  if n == 0:
    zero = 1
  else:
    zero = fib_num[n-1]
  one = fib_num[n]
  print(zero, one)
