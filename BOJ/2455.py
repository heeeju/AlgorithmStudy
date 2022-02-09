cnt = 0
max_cnt = 0
for _ in range(4):
    out, come = map(int, input().split())
    cnt -= out
    cnt += come
    if cnt > max_cnt:
      max_cnt = cnt

print(max_cnt)
