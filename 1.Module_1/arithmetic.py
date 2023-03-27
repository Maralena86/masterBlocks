import math
"Make operation (3+2/2*5)°"

result = (3 + 2) / (2 * 5)
result = math.pow(result, 2)
print(result)

numPositive = int(input("Give me a positive number: "))
result2 = int(((numPositive + 1)*numPositive)/2)
print(str(result2))

num1 = int(input("Give me the first number to divide: "))
num2 = int(input("Give me the second number to divide: "))

result = int(num1 / num2)
rest = int(num1 % num2)

print("The division between "+ str(num1)+ " and "+ str(num2)+ " is " + str(result) + " and the rest is " + str(rest))

