for _ in range(int(input())):
    for i, bit in enumerate(bin(int(input()))[:1:-1]):
        if bit == '1':
            print(i, end=" ")
