w, h, b = map(int, input().split())
storage = ((w * h * b / 8) / 1024) / 1024

print(f'{storage:.2f}', 'MB')