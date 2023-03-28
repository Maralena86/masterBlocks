password = input("Create your password: ")
if ("*" in password or "#" in password) and ("a" in password or "e" in password or "i" in password):
    print("password validated")
else:
    print("password can't be validated")