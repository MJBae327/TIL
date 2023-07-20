# n = int(input())
# i = 0

# while True:
#     i += 1
#     if i % 3 == 0:
#         continue
#     print(i, end=' ')
#     if i == n:
#         break

n = int(input())

for i in range(0, n + 1):
    i += 1
    if i > n:
        break
    if i % 3 == 0:
        continue
    print(i, end=' ')


# 6079번
# n = int(input())
# h = 0

# for i in range(0, n + 1):
#     h += i
#     if h >= n:
#         print(i)
#         break
