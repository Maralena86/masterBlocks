"Take a letter from the user and proove that's upper or lower"

letterToTest = str(input("Choice a letter from the alphabet: "))
if(letterToTest.isalpha()):
    if(letterToTest == letterToTest.lower()):
        print("It's a lowercase")
    elif(letterToTest == letterToTest.upper()):
        print("It's an uppercase")
else:
    print("That's not a letter")
