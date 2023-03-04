print ("-------------------------------------------")
print ("-----------BIENVENIDO AL PROGRAMA----------")
print ("-------------------------------------------")

X = int(input("Ingrese el tiempo que duró la llamada: "))
W = 300

if X <= 3 :
    rta = "El costo es: " + str(W)

else :
    Y = (X-3)
    Z = (Y*50)
    A = (W + Z)
    rta = A

print ("El costo de la llamada es :" + str (rta)) 

print ("-------------------------------------------")
print ("-------------au revoir mon pote------------")
print ("-------------------------------------------")
