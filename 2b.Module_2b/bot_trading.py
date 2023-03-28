'Make a bot that takes a montant and advise the movement to do: buy ifs less than 100, hold between 100 and 150 or sell if its more than 150'

money_entry = float(input("How montant you wil gonna entry? "))

if money_entry < 100:
    print("Buy!!! 💵")
elif money_entry >= 100 and money_entry <= 150:
    print("Hold!! 💸")
else:
    print("Sell!!! 💰")