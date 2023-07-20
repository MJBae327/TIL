# array = [
#     [1, 2, 3],
#     [4, 5, 6],   # 행과 열이 명확하게 구분되도록 2차원 리스트를 작성하는 것이 좋음
#     [7, 8, 9]
# ]

# #1. 인덱싱하여 3을 출력해보세요.
# print(array[0][2]) # 첫번째 인덱스는 행, 두번째 인덱스는 열

# #2. 인덱싱하여 7을 출력해보세요.
# print(array[2][0])


# # 2차원 리스트를 입력 받는 방법
# rows = int(input("행의 개수를 입력하세요. "))
# matrix = []

# for i in range(rows):
#     row = list(map(int, input().split()))
#     matrix.append(row)

# matrix = [list(map(int, input().split())) for _ in range(rows)]

# for row in matrix:
#     print(row)


# # 튜플을 사용하는 예시: 방향배열
# def move_around(position):
#     x, y = position
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 상, 하, 좌, 우
#     directions_2 = [(-1, 1), (1, -1), (1, 1), (-1, -1)] # 대각선 방향

# # range -> 주로 반복문과 함께 쓰인다
# range(5)
# # range(end) : 0부터 end-1까지 1만큼 증가
# for i in range(5): # 5번 반복하는 반복문

# range(2, 5)
# # range(start, end) : start부터 end-1까지 1만큼 증가
# range(1, 10, 2)
# # range(start, end, step)
# # start < end : start부터 end-1까지 step만큼 증가
# # start > end : start부터 end+1까지 step만큼 감소

# my_dict = {
#     'a1' : {'b1' : 1, 'b2' : 2, 'b3' : 3},
#     'a2' : {'b1' : 4, 'b2' : 5, 'b3' : 6},
#     'a3' : {'b1' : 7, 'b2' : 8, 'b3' : 9}
# }

# # value 5를 출력해보세요
# print(my_dict['a2']['b2'])

# # value = my_dict['a2']['b2']
# value = my_dict.get('a2').get('b2')
# print(value)

# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {4, 5, 6, 7, 8, 9}

# #합집합 출력
# print(set_1 | set_2)
# #차집합 출력
# print(set_1 - set_2)
# #교집합 출력
# print(set_1 & set_2)

# # 세트의 사용 예시 -> 로또 번호 추첨
# import random

# lotto_set = set()

# while len(lotto_set) < 6:
#     number = random.randint(1, 45)
#     lotto_set.add(number)

# lotto_list = list(lotto_set)
# lotto_list.sort()
# print(lotto_list)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))
print(a is b)

print(int(float('3.5')))

numbers = [1, 2, 3, 4, 5]

total = 0
for number in numbers:
    total += number

print(total)

a = [1, 2, 3]
b = [1, 2, 3]
# 서로 다른 객체. 서로 다른 메모리 주소를 가지고 있음

print(a == b) # True
print(a is b) # False


vowels = 'aeiou'

print(('a' and 'b') in vowels) # a or b는 a, a and b는 b
# 코드가 왼쪽부터 진행되므로 a가 참이라는 것만으로 참거짓이 판별되지 않음->b
print(('b' and 'a') in vowels)

print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)

print(5 or 3)
print(3 or 0)
print(0 or 3)
print(0 or 0)

# 함수 정의, 함수 선언
'''
def 함수명(매개변수):
    code...     # 함수 바디
    code...     # 함수 바디
    return 반환값
'''

# 함수 호출
'''
함수명(함수인자)
'''

# 매개변수는 있을 수도 있고 없을 수도 있다.
# 반환값은 있을 수도 있고 없을 수도 있다.
# --> 총 4가지 유형의 함수가 존재

def get_sum(num1, num2):
    return num1 + num2

num1 = 5
num2 = 3

result = get_sum(num1, num2)
print(result)

#1. 매개변수가 없는 함수로 변형 -> 출력결과는 같게
def get_sum():
    num1, num2 = 5, 3
    return num1 + num2

result = get_sum()
print(result)

#2. return 반환값이 없는 함수로 변형 -> 출력결과는 같게
def get_sum(num1, num2):
    result = get_sum(num1, num2)
    print(result)

num1 = 5
num2 = 3
# get_sum(num1, num2)


# map() 함수를 사용하여 numbers 리스트에 각 요소가 제곱된 값들로 이루어진 새로운 리스트 생성
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)