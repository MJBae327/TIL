r, g, b = map(int, input().split())
for i in range(r):
    for m in range(g):
        for n in range(b):
            print(i, m, n)
print(r * g * b)