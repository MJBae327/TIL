def increase_user():
    pass

def create_user():
    keys = ['name', 'age', 'address']
    name, age, address = input().split()
    values = name, int(age), address
    user_info = dict(zip(keys, values))

    users_info = []
# while len(users_info) == 0:
#     for user in user_info:
#         users_info.append(user)
#         len(users_info) -= 1

    print(users_info)
    # for b in range(len(users_info)
    #     print(user_info[b]['name']+'님 환영합니다!')
                
create_user()