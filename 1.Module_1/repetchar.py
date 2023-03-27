string = str(input('Write 5 characteres'))
stringRepet = []
for i in range(len(string)): 
    stringRepet.append(string[i]*2)
print("".join(stringRepet)) 
