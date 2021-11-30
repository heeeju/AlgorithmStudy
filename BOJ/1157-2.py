str = input().upper()
searchKeys = list(set(str))

cnt = []
for key in searchKeys:
  cnt.append(str.count(key))

if cnt.count(max(cnt)) == 1:
  print(searchKeys[cnt.index(max(cnt))])
else:
  print("?")
