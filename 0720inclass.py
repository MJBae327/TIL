# packing_values = 1, 2, 3, 4, 5
# print(packing_values)

# numbers = [1, 2, 3, 4, 5]
# a, *b, c = numbers # *: 패킹연산자로 활용
# print(a)
# print(b)
# print(c)

# print('hi', 'hello', 'goodbye', sep = '-')
# print('hi', end=' ')
# print('hello')

# # *를 언패킹 연산자로 활용
# names = ['kai', 'jane', 'bob']
# print(*names)

# # **: 딕셔너리 언패킹 연산자
# def my_function(x, y, z):
#     print(x, y, z)
# dict_values = {'x' : 1, 'y' : 2, 'z' : 3}
# my_function(**dict_values)


# import math
# print(math.pi)
# print(math.sqrt(4))

# from math import pi, sqrt
# print(pi)
# print(sqrt(4))

# import random
# print(random.randint(1, 10))

# from random import *
# print(randint(1, 10))

# import my_package.math.my_math as my_math

# print(my_math.add(1, 2))

# from my_package.math import my_math
# from my_package.statistics import tools

# print(my_math.add(1, 2))
# print(tools.mod(1, 2))

# import requests

# url = 'https://random-data-api.com/api/v2/users'

# response = requests.get(url).json()
# print(response)

# #실습) United States를 출력해 보세요.
# print(response['address']['country'])
# print(response.get('address').get('country'))

# 조건문(if문) - 조건식이 참이면 code를 실행
'''
if 조건식:
    code...
elif 조건식:
    code...
else:
    code...
'''

# 조건식에는 비교연산, 논리연산, 멤버연산 등...
# if의 부정이 elif, elif의 부정이 else

# dust = int(input())

# if dust > 150:
#     print('매우나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')

# 2번째 elif의 범위는 80 < dust <= 150
# 3번째 elif의 범위는 30 < dust <= 80

# # 실습 1 정수를 입력받아 짝수면 'EVEN', 홀수면 'ODD' 출력
# num = int(input())

# if num % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")
# # 실습 2 윤년 판별하기, 윤년이면 'leap year', 그렇지 않으면 'common year' 출력하기
# # 윤년의 조건1: 연도가 4로 나누어 떨어지지만 100으로는 나누어 떨어지면 안된다.
# # 윤년의 조건2: 연도가 400으로 나누어 떨어진다
# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("leap year")
# else:
#     print("common year")

# '''
# for 변수 in 반복 가능한 객체(iterable):
#     code...
# '''

# # 반복 가능한 객체 -> 리스트, 튜플, 문자열, range ... 등
# # 중첩 for문 실습 1. 구구단 출력
# '''
# <2단>
# 2 * 1 = 2
# 2 * 2 = 4
# ....
# ...
# <9단>

# '''
# for i in range (2, 10):
#     print(f'<{i}단>')
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j:>2}')
#     print()


# # 실습 2. 정수 n을 입력받아 n단의 왼쪽 직각 이등변 삼각형을 그리는 프로그램 작성
# '''
# n : 5
# *
# **
# ***
# ****
# *****
# '''
# n = int(input())
# for i in range(1, n+1):
#     print("*" * i)

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end='')
#     print()




# # while 문
# # 실습 1. continue 이용하여 1부터 10까지 정수 중 홀수만 출력하기
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     else:
#         print(i, end = ' ')
    

# # 실습 2. break 이용하여 'Shall we close? (y/n)' 문구에 y를 입력해야
# # 반복문을 탈출하고 'The end'를 출력하는 프로그램 작성

# while True:
#     ans = input("Shall we close? (y/n)")
#     if ans == 'y':
#         print("The end")
#         break

# # 실습 3 정수를 입력받아 그 정수가 몇 자릿수 숫자인지 알아내는 프로그램 작성
# num = int(input())
# cnt = 0
# while num > 0:
#     cnt += 1
#     num //= 10
# print(cnt)

# import math
# numbers = [1, 4, 9, 16, 25]

# sqrt_numbers = []
# for number in numbers:
#     sqrt_numbers.append(math.sqrt(number))

# print(sqrt_numbers)

# # list comprehenstion으로 180~182
# sqrt_numbers = [math.sqrt(number) for number in numbers]
# print(sqrt_numbers)

# # 실습 2. if 추가 짝수만 추가해보세요
# sqrt_numbers = [math.sqrt(number) for number in numbers if number % 2 == 0]
# print(sqrt_numbers)


