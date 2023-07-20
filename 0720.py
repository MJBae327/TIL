# num = int(input("숫자를 입력하세요 : "))

# # if statement
# # num이 홀수라면
# # if num % 2 == 1:
# if num % 2:     # 결과 1이 True이기 때문에 (적은양의 코드가 아니라 명시적인 코드가 더 좋은 코드임)
#     print("홀수입니다")
# # num이 홀수가 아니라면(짝수면)
# else:
#     print("짝수입니다")



# numbers = [4, 6, 10, -8, 5]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)

# outers = ['A', 'B']
# inners = ['c', 'd']

# for outer in outers:
#     for inner in inners:
#         print(outer, inner)


# a = 0

# while a < 3:
#     print(a)
#     a += 1

# print("끝")

# number = int(input("양의 정수를 입력해주세요.: "))

# while number <= 0:
#     if number < 0:
#         print("음수를 입력했습니다.")
#     else:
#         print("0은 양의 정수가 아닙니다.")
#     number = int(input("양의 정수를 입력해주세요.: "))

# print("잘했습니다!")


# # 0~9 요소를 가지는 리스트 만들기
# # 1. 일반적인 방법
# new_list = []
# for i in range(10):
#     new_list.append(i)
# print(new_list)

# # 2. list comprehension
# new_list_2 = [i for i in range(10)]
# print(new_list_2)


# # 1. 일반적인 방법
# new_list = []
# for i in range(10):
#     if i % 2 == 1:
#         new_list.append(i)
# print(new_list)

# # 2. list comprehension
# new_list_2 = [i for i in range(10) if i % 2 == 1]
# print(new_list_2)

# new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
# print(new_list_3)


# 리스트를 생성하는 3가지 방법 비교
# 정수 1, 2, 3을 가지는 새로운 리스트 만들기

# numbers = ['1', '2', '3']

# # for loop
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers) #[1, 2, 3]

# # map
# new_numbers_2 = list(map(int, numbers))
# print(new_numbers_2)

# # list comprehension
# new_numbers_3 = [int(number) for number in numbers]
# print(new_numbers_3)

# enumerate
result = ['a', 'b', 'c']

print(enumerate(result))
print(list(enumerate(result)))

for index, elem in enumerate(result):
    print(index, elem)