# PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# # 반지름
# R = 15

# print('원주율 : ', PI)
# print('반지름 : ', R)
# print('원의 둘레 : ', PI * 2 * R)
# print('원의 넓이 : ', R ** 2 * PI)

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


increase_user()
print(number_of_people)
