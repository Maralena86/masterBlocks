name = input("What's your name? ")
averageNote = int(input("What's your average note? "))
age = int(input("What's your age? "))

if (age >= 17 or age <= 21) and (averageNote >=8):
    input("Hi " + name +" you can acces to scolarship! congratulations!")
else:
    input("Sorry, you can't acces to the scolarship.")