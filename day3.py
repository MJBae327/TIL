# 함수 정의
def greet(name):
    """임력된 이름 값에
    인사를 하는 메세지를 만드는 함수
    """
    message = 'Hello, ' +name
    return message

# 함수 호출
result = greet("Alice")
print(result)


def add_numbers(x, y): #x와 y는 매개변수(parameter) -> 정의할 때는 매개변수
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자(argument) -> 호출될 때 실제 값
print(sum_result)


# 위치인자
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet("Alice", 25) # 안녕하세요, Alice님! 25살이시군요.

# 기본인자
def greet(name, age = 30):
    # 사용자가 age를 입력하지 않으면 기본으로 30이라고 하겠다!(사용자 입력은 선택적)
    print(f'안녕하세요, {name}님, {age}살이시군요')

greet("Bob") # 안녕하세요, Bob님! 30살이시군요.
greet("Charlie", 40) # 안녕하세요, Charlie님! 40살이시군요.

# 키워드 인자
def greet(name, age):
    print(f'안녕하세요, {name}님!, {age}살이시군요.')

greet(age = 35, name = "Dave",) # 안녕하세요, Dave님! 35살이시군요.
'''인자의 순서는 중요하지 않다.
다만 greet(age = 35, "Dave")라고 하면
positional argument follows keyword argument라는 syntax error가 뜸
꼭 위치 인자 뒤에 키워드 인자 써주어야 한다.
'''

# 임의의 인자 목록
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total}')

'''
(1, 2, 3)
합계: 6
'''
calculate_sum(1, 2, 3) #(1, 2, 3)
                       # 합계: 6

# 임의의 키워드 인자 목록
def print_info(**kwargs):
    print(kwargs)

print_info(name = "Eve", age = 30, address = "Korea") #{'name': 'Eve', 'age': 30, 'address': 'Korea'}


# def func():
#     num = 20
#     print("local", num)

# func()

# print("global", num)

a = 1
b = 2

def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)

    local(500)
    print(a, b, c)

enclosed()
print(a, b)


def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
    return n * factorial(n - 1)

# 팩토리얼 계산 예시
result = factorial(5)
print(result)  # 120


numbers = [1, 2, 3]
result = map(str, numbers)

print(result) # <map object at 0x00000210044EBEB0>
print(list(result)) # ['1', '2', '3']

result = []
for number in numbers:
    result.append(str(number))

print(result)

girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)

print(pair) # <zip object at 0x0000021F495FB640>
print(list(pair)) # [('jane', 'peter'), ('ashley', 'jay')]


#두 개의 리스트를 딕셔너리로 변환하기
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}


# map + lambda //일회성으로 쓰는 예
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)


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