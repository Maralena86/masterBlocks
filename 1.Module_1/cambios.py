import numpy 
'Casa de cambios cambia euros a dolares. La casa se queda con 10% y el usuario recibe el valor restante'
dolar = float(1.2)
euro = float(input('Euro= '))

cambio = float(dolar * euro)
total = cambio * 0.1
totalUsuario = float(cambio - total)

print ('Haz cambiado ' + str(euro) + ' euros, recibiras: ' + str(totalUsuario) + ' dolares la casa toma ' + str(total) )
