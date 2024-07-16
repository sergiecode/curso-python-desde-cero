# TUPLA: colección (array) que permite almacenar múltiples elementos en una sola variable
# Característica: Colección ordenada e inmutable de elementos (cada elemento tendrá un índice)

# indices:       0          1        2        3           4       5
vehiculos = ("Bicicleta", "Moto", "Auto", "Camioneta", "Avion", "Barco")

longitud = len(vehiculos) # con len podemos saber la longitud de la tupla
tipo = type(vehiculos) # nos indica que es de tipo <class 'tuple'>
tuplaConstructor = tuple(("Esta", "es", "una", "tupla")) # con el constructur de tupla podemos iniciar una

# Acceso a través de indices:
elemento1 = vehiculos[1]
elemento2 = vehiculos[-4]
rango = vehiculos[3:5]
desdeInicio = vehiculos[:3]
hastaFinal = vehiculos[3:]

# ¿Cómo puedo hacer para obtener una tupla con las características que yo necesito? [Truco para modificar tupla]

listaVehiculos = list(vehiculos) # en una nueva variable volcar la tupla como lista
listaVehiculos[3] = "Camión" # hacer el cambio que queríamos hacer
listaVehiculos.append("Crucero")
vehiculos = tuple(listaVehiculos) # asignar a la tupla la lista modificada convertida en tupla

# Desempaquetamiento:
(a,b,c,d,e,f,g) = vehiculos # se asignará cada elemento a una variable correspondiente a la posicion
(bici,moto, *cuadroRuedas, avion, barco, crucero) = vehiculos # con el asterisco podemos agrupar parte del desempaquetamiento 

# Recorrer las tuplas con bucles

for vehiculo in vehiculos:
    print(vehiculo)

for i in range(len(vehiculos)): # De esta forma podemos tener el índice del elemento iterable al recorrer la tupla 
    print(f"{i+1}. {vehiculos[i]}")

[print(tecnologia) for tecnologia in vehiculos] # Este sería el shorthand para una impresión de tupla iterable

# Join de tuplas (unir tuplas)

citricos = ("naranja", "limon", "pomelo")
tropical = ("papaya", "coco")

frutas = citricos + tropical # con esto unimos las dos tuplas en una nueva tupla

