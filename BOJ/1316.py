n = int(input())
words = [input() for i in range(n)]
count = 0
for w in words:
  check = [0 for i in range(26)]
  flag = 0
  for i in range(len(w)):
    if i != 0 and w[i-1]==w[i]:
      continue
    elif check[ord(w[i])-97]==0:
      check[ord(w[i])-97] = 1
    else:
      flag = 1
      break
  if flag==0:
    count+=1

print(count)
