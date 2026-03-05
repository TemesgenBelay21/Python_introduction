
user_name = "admin"
user_password = "1234"

print("pls enter ur user name and password")

name = input("name: ")
password = input("password: ")

if user_name == name and user_password == password:
    print("access granted")
else:
    print("access denied")
