"Take 3 valeurs that belong to the table's messures to build a roof. Proove that's possible to do it"

x,y,z = 10, 20, 60

"For that it's necessary that one table's value it's greatest than the other' addition "

if(x>(y+z)or y >(x+z) or z > (x+y)):
    print("Its possible to build the roof!")
else: 
    print("It's not possible to build the roof :(")