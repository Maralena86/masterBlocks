first_number =int(input("First number: "))
second_number =int(input("Second number: "))
third_number =int(input("Third number: "))

if (first_number+ second_number)== third_number:
    print("The third one: " +str(third_number) + " has the same value that the first and second number " + str(first_number) + " and "+ str(second_number))
elif (third_number+ second_number)== first_number:
    print("The second one: " +str(first_number) + " has the same value that the first and third number " + str(first_number) + " and "+ str(third_number))
elif (third_number+ first_number)== second_number:
    print("The second one: " + str(second_number) + " has the same value that the first and third number " + str(first_number) + " and "+ str(third_number))
else:
    print("Not relation between the numbers")
