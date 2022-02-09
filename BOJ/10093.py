a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

if b == a:
    print(0)
else:
    print(b-a-1)
    for i in range(a+1, b):
        print(i, end = ' ')
