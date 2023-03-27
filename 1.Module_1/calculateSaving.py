"Make a saving's account calculate"
'Create a welcome message'
name = str(input("What's your name? "))
print("Welcome "+ name)

' Ask for hours worked and money for hour maked'
moneyGain = float(input("How many tou won per hour? "))
hoursWorked = int(input("How many hours you worked? "))

'Calculate the week and year salary'
weekSalary = float(hoursWorked * moneyGain)
yearSalary = float(weekSalary * 50)

'Return the result'
print(str(name)+ " You have a salary of " + str(yearSalary)+ "€ this year " )

'Calculate expenses from year and month'

weekExpenses = float(input("How much you spend for week? "))
yearExpenses = float(weekExpenses * 50)

'with the information calculate the savings in the year'
yearSavings = yearSalary - yearExpenses

print("Your expenses this year were "+ str(yearExpenses) + "€ and you have save " + str(yearSavings))

