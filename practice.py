# 진법 변경 (10진수 -> n진수)
print(bin(12))
print(oct(12))
print(hex(12))

print(2 / 3)

print(5 / 3)

a = 3.2 - 3.1
b = 1.2 - 1.1

# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10)

# 2. math 모듈 활용
import math
print(math.isclose(a, b))

# 지수(제곱하는 횟수) 표현 10^
print(314e-2) # 3.14
print(314e2) # 31400.0

# 철수야 '안녕'
print('철수야 \'안녕\'')

'''
이 다음은 엔터
입니다.
'''
print('이 다음은 엔터\n입니다.')

# f-string
bugs = 'roaches'
counts = 13
area = 'living room'

# Debugging roaches 13 living room
print(f'Debugging {bugs} {counts} {area}')

# f-string 응용
greeting = 'hi'
print(f'{greeting:>10}')
print(f'{greeting:^10}')
print(f'{3.141592:.4f}')

my_str = 'hello'
print(my_str[::-1])

my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))
print(my_list[4][-1])
print(my_list[-1][1][0])

# 불변과 가변
my_str = 'hello'
my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)