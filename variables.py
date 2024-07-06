# Variables:
# Es un contenedor para almacenar valores de datos.
# Este contenedor va a tener un nombre.
# Es creada la primera vez que se le asigna un valor

# NOMBRES ADMITIDOS DE VARIABLES

# 1. Puede empezar con una letra o un guión bajo (underscore)
mivariable = "texto"
_mivariable = "otro texto"

# 2. No puede iniciar con un número
### 5variable = "texto"

# 3. Sólo pueden contener caracteres alfanuméricos y guiones bajos (A-z 0-9 _)
miVariable123_ = "texto"
_123miVariable_123 = "texto"

# 4. CaseSensitive (no solo al comienzo sino en general)

miVariable = "otro texto"
MiVariable = "otro texto"

# 5. No se puede utilizar palabras reservadas de Python (keywords)

asd123 = "informacion"

#####################

# Convenciones de escritura de variables

# Camel Case
camelCase = "Comienza con minúscula y cada palabra siguiente comenzará con mayúscula"

# Pascal Case
PascalCase = "Comienza con mayúscula y cada palabra siguiente comenzará con mayúscula"

# Snake Case
snake_case = "Se usan las palabras en minúscula y las palabras son separadas con guiones bajos"

#####################

# Multiasignación

x, y, z = 5, 7, 9
a = b = c = "Sergie Code"

# Desde colecciones
frutas = ["naranja", "banana", "mandarina"]
m, n, o = frutas

# Uso de print y salidas:

txt = "Curso"
txt2 = "de "
txt3 = "Python"

num1 = 2
num2 = 4
num3 = 6

# Variables globales vs Variables de Scope

variableGlobal = "Esta variable va a estar disponible para todo el programa"

def funcion():
    global variableDeScope
    variableDeScope = "Esta variable sólo estará disponible dentro del alcance de la función"
    variableGlobal = "Este valor es sólo para dentro de la función y luego recupera su valor"
    print(variableGlobal)
    print(variableDeScope)

funcion()

print(variableGlobal)
print(variableDeScope)