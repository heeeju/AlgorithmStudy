factorial = [1 for i in range(13)]

def multiply(n):
  if n <= 1:
    return 1
  else:
    if factorial[n] == 1:
      return n * multiply(n-1)
    else:
      return factorial[n]

n = int(input())
print(multiply(n))
