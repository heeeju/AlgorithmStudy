case = input()
for i in range(case):
    num = input()
    bits = []
    while num != 0:
        num = num // 2
        bits.append(num%2)
    for i, bit in enumerate(bits):
        if bit == 1:
            print(i, end=' ')
