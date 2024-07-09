### CONDICIONALES (if, elif, else)
# Es la estructura que nos permite tomar un flujo u otro según una condición

# La palabra reservada if es obligatoria en la estructura condicional pero elif y else son opcionales

a = 5
b = 9
c = 7

if a > b: # Si cumple esta condición hace 
    print(f"{a} es mayor que {b}") # estas lineas de código
elif c > b: # Si no cumple la primera condición pero cumple esta realiza:
    print(f"{c} es mayor que {b}") # estas otras líneas de código
else: # Si no cumplió ninguna de las condiciones anteriores
    print(f"{a} es menor que {b} y {c} es menor que {b}") # realiza estas últimas líneas de código


### Ejemplo:

# Objetivo entrar al boliche

edad = 61

if edad >= 18 and edad <= 60:
    print("Puedes entrar al boliche")
else: 
    if edad < 18:
        print("No tienes la edad suficiente para ingresar al boliche")
    else:
        print("Este boliche sólo admite personas hasta 60 años")


### SHORTHANDS

a = 5
b = 2

if a > b: print(f"{a} es mayor que {b}") ## Shorthand del If solo

# Ejecución si es verdadero | condición | Ejecución si es Falso
print("B es mayor que A") if b > a else print("A es mayor que B") ## Shorthand de If + Else 

