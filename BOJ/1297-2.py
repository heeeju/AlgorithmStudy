d, h, w = map(int, input().split())
a = (d**2 / (h**2 + w**2))**0.5

print(int(h*a), int(w*a))
