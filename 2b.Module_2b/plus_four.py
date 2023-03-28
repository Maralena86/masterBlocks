first_number =int(input("First number: "))
second_number =int(input("Second number: "))
third_number =int(input("Third number: "))
fourth_number =int(input("Fourth number: "))

if(first_number > second_number) and (first_number >third_number) and (first_number > fourth_number):
    print("The first number is the greater")
else:
    if (second_number > first_number) and (second_number >third_number) and (second_number > fourth_number):
        print("The second is the greatest")
    elif (third_number >first_number) and (third_number >second_number) and (third_number >fourth_number):
        print("The third is the gratest")
    else:
        print("The fourth is the greatest")