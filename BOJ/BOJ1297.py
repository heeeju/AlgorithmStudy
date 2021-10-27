D, H, W = map(int, input().split())

RH = int((H*D) / (((H**2) + (W**2)) **(1/2)))
RW = int((W*D) / (((H**2) + (W**2)) **(1/2)))

print(RH, RW)
