# decimal = 10
# # 1. 2진수로 출력해 보세요
# print(bin(decimal)[2:])
# # 2. 8진수로 출력해 보세요
# print(oct(decimal)[2:])
# # 3. 16진수로 출력해 보세요
# print(hex(decimal)[2:])

# 부동 소수점: 컴퓨터의 용량이 한정되어있기 때문에 나타남
# 부동 소수점 값을 출력 할 때 f-string을 활용하여 부동소수점의 정확도 제어가능
# a = 3.2 - 3.1
# b = 1.2 - 1.1

# print(f'{a:.1f}')
# print(f'{b:.1f}')

print(314e-2)
# 산술 연산자를 사용하여 표현식을 바꿔보세요.
print(314 * 10 ** -2)

# greeting = 'hi'
# print(f'{greeting:>10}')
# print(f'{greeting:^10}')
# print(f'{greeting:<10}')

# IM형 문자열 파싱문제 많이 나옴..

# greeting = "hello world"

# # 1. 인덱싱 -> 알파벳 w를 출력해 보세요.
# print(greeting[6])
# # 2-1. 슬라이싱 -> hello를 출력해 보세요.
# print(greeting[:5])
# # 2-2. 슬라이싱 -> world를 출력해 보세요.
# print(greeting[6:])
# # 2-3 슬라이싱 -> 거꾸로 출력해 보세요.
# print(greeting[::-1])
# # 3. 내장함수를 사용해서 문자열의 길이를 출력해 보세요.
# print(len(greeting))
# # 4. for 문을 활용하여 hello world를 출력해 보세요.(2가지 방법)
# for i in greeting[0:]:
#     print(i, end='')
# for i in range(len(greeting) + 1):
#     if i < len(greeting):
#         continue
#     if i == len(greeting):
#         print('\n'+greeting[:i])