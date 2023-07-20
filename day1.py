# char = input()
# char = input("문자 한개를 입력하세요!!")
# num = int(input())
# print(char, num)

# char1, char2 = input().split() #공백을 기준으로 분리해서 입력받음
# num1, num2 = map(int, input().split()) #공백을 기준으로 정수 두개를 입력받음

# year, month, day = map(int, input().split('.'))

# num_list = list(map(int, input().split()))

name = input()
age = int(input())
height = float(input())
# 1. 포맷 코드
print("저의 이름은 %s, 나이는 %d, 키는 %.2f" %(name, age, height))
# 2. f-string
print(f"저의 이름은 {name}, 나이는 {age}, 키는 {height:.2f}")
# 3. .format()
print("저의 이름은 {}, 나이는 {}, 키는 {:.2f}" .format(name, age, height))
