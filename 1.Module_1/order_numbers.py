number = int(input("What's you number? ")) 
numberString = str(number)
string = [*numberString]
strNew = []
j = len(string)-1
for i in range(len(string)):
    print(string[i])
    strNew.append(string[j])
    j= j - 1
print(''.join(strNew))

