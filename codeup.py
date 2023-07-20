n = int(input())
for i in range(1, n + 1):
    if n < 30:
            if i % 10 == 3:
                print("X")
            elif i % 10 == 6:
                print("X")
            elif i % 10 == 9:
                print("X")
            else:
                print(i)
    if n >= 30:
            if 0 <= i % 30 <= 9:
                if i % 10 == 3:
                    print("XX")
                elif i % 10 == 6:
                    print("XX")
                elif i % 10 == 9:
                    print("XX")
                else:
                    print("X")
            else:
                if i % 10 == 3:
                    print("X")
                elif i % 10 == 6:
                    print("X")
                elif i % 10 == 9:
                    print("X")
                else:
                    print(i)