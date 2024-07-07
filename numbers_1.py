####### NUMBERS

# int (Integer): Número entero
numero_entero = 10

# float: Número decimal
numero_decimal = 5.75

# complex: numero complejo (parte entera y otra parte imaginaria)
numero_complejo = 5 + 2j

print(numero_entero) #
print(type(numero_entero)) # int

print(numero_decimal) #3.14
print(type(numero_decimal)) #float

print(numero_complejo)  # (5+2j)
print(type(numero_complejo))  # complex

###### CASTEO

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

print(decimal_desde_entero)
print(entero_desde_decimal)
print(complejo_desde_entero)
print(complejo_desde_decimal)

####### RANDOM

import random

aleatorio = random.randrange(1,10) # El número de stop no es incluyente
aleatorio_par = random.randrange(2,11,2) # Número par del 2 al 10 (incluído)
aleatorio_impar = random.randrange(1,10,2) #Número impar del 1 al 9 (incluído)

print(aleatorio)
print(aleatorio_par)
print(aleatorio_impar)