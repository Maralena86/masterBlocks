"Ask for the password and if it's correct message of welcome, if not message error and ask again"
password = "parini345"
password_log = input("Enter the password: ")

if password_log.lower() == password:
    print("Hey, Welcome!!")
else:
    password_log = input("That's not correct, try again!!: ")
    if password_log.lower() == password:
        print("Now you can enter, Welcome!")
    else: 
        print("Tht's wrong, acces refused")
