'''Convert in seconds the times passed: 
annah Neise: 8 minutos 3 segundos y 10 centésimas 
Jackie Narracott: 12 minutes 7 seconds y 8 centésimas 
Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
'''
"Take the information for the runner"
name = str(input("What's the name's finaliste?"))
minutes = float(input("How much minutes?"))
seconds = float(input("How much seconds?"))
cents = float(input("How much cents?"))
"Calculate the time in seconds:"
total = float((60 * minutes)+ seconds + (cents * 0.1))
"Calculate the velocity"
velocity = float(100/total)

print("The total time was: " + str(total) + " seconds and the velocity was: " + str(velocity) + " metres par s")
