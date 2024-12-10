users = []
user = {}
name = input("Enter the user name :")
age = input("Enter the user age :")
sex = input("Entert the user sex :")

user = {"name":name, "age":age, "sex":sex}

users.append(user)

for user in users:
    if user.get('sex')== 'female':
        pass
    else:
        print(user)
