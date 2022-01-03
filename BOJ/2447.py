#메모리 67592KB
#시간 3488ms
result = []

def erase(y, x, n):
  #중간 비우기
  for i in range(y*n + n//3, y*n + n//3*2):
    for j in range(x*n + n//3, x*n + n//3*2):
      result[i][j]=' '
  #제일 작은 경우인지 확인 (n==3)
  if n == 3:
    return
  #8개 반복
  n //= 3
  for i in range(0, 3):
    for j in range(0, 3):
      erase(y*3+i, x*3+j, n)


n = int(input())
result = [['*' for i in range(n)] for j in range(n)]
erase(0, 0, n)

for i in range(n):
  for j in range(n):
    print(result[i][j], end='')
  print()
