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