users = []
user = {}
response = 'y'
while response.lower() == 'y':
    name = input("Enter the user name :")
    age = input("Enter the user age :")
    sex = input("Entert the user sex :")
   
    user = {"name":name, "age":age, "sex":sex}
    users.append(user)

    response = input("Enter y to continue and other to exit:")

females= []
males = []

for user in users:
    if user.get('sex')== 'female':
        females.append(user)
        
    else:
        males.append(user)

print("males " + males)
print("females "+ females)
