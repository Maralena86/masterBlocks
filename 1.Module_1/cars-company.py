'Company cars has 3 kind of cars, every car has his own price and commision. Calculate the total comission of the sells in the month'

rbm1CarPrice =  float(20000)
rbm1CarCommision = float(0.03 * rbm1CarPrice)

rbmPlusPrice = float(35000)
rbmPlusCommision = float(0.05 * rbmPlusPrice)

rbmFourWheelPrice = float(60000)
rbmFourWheelCommision = float(0.07 * rbmFourWheelPrice)


totalCarsSelledRbm1 = float(input("How many rbm1 you selled?"))
totalCommisionRbm1 = float(rbm1CarCommision * totalCarsSelledRbm1)



totalCarsSelledRbmPlus = float(input("How many rbm Plus you selled?"))
totalCommisionRbmPlus = float(rbmPlusCommision * totalCarsSelledRbmPlus)


totalCarsSelledRbmFourWheel = float(input("How many rbm Four Wheel you selled?"))
totalCommisionRbmFourWheel = float(rbmFourWheelCommision * totalCarsSelledRbmFourWheel)


totalCarsComissionSelled = totalCommisionRbm1 + totalCommisionRbmPlus  + totalCommisionRbmFourWheel

totalCarsSelled = totalCarsSelledRbm1 + totalCarsSelledRbmPlus + totalCarsSelledRbmFourWheel

print("Your commision for the month is: "+ str(totalCarsComissionSelled) +" and you selled " + str(totalCarsSelled) + " cars")