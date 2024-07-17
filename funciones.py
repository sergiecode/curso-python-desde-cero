# Función es un bloque de código autónomo que se ejecuta cuando lo llamamos
# Nos va a servir para atomizar y reutilizar código optimizando el mismo

# Parámetros son la lista de variables dentro de los paréntesis
# Argumentos son los valores que le enviamos a la función cuando es llamada

             # parámetros = variables
def funcion(profesor, curso, femenino):
    profesion = "el profesor"
    if femenino:
        profesion = "la profesora"
    print(f"El curso de {curso} lo dará {profesion} {profesor}")

          # Argumetos = valores
funcion("Sergie Code", "Python desde Cero", False)
funcion("Pedrito", "Cocina", False)
funcion("Marina", "Manejo", True)
funcion("Mercedes", "Bajo", True)

# Variables por defecto / Esto nos dará la posibilidad de NO enviar ese argumento (opcional)

def decir_pais(pais = "Argentina"):
    print(f"El nombre de mi país es {pais}")

decir_pais("México")
decir_pais()

# Retornar valores

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a // b

resultado_suma = suma(3,2)
resultado_resta = resta(5,3)
resultado_multiplicacion = multiplicacion(5,5)
resultado_division = division(10,2)

print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)

# Argumentos Arbitrarios (mandar múltiples argumentos según dependa)
# Hay que tener cuidado de que esté bien manejado para no dar errores

def llamar_alumnos(*alumnos):
    print(f"Mi mejor alumno es {alumnos[0]}")
    print(f"Mi alumna más divertida es {alumnos[2]}")

llamar_alumnos("Ricardo", "Antonieta", "Beatriz", "Lionel")

# Argumento clave / key arguments

def cursos(curso1, curso2, curso3):
    print(f"El primer curso que daré será el de {curso1}")
    print(f"el siguiente será el curso de {curso2}")
    print(f"y para finalizar daré el curso de {curso3}")

cursos(curso3 = "Java", curso2 = "CSS", curso1 = "HTML") # Indicaremos a que paráemtro corresponde cada argumento

# Argumentos claves arbitrarios

def llamar_alumno(**alumno):
    print(f"El apellido del alumno es {alumno["apellido"]}, y su nombre es {alumno["nombre"]}")

llamar_alumno(apellido = "Perez", nombre = "Tobías", edad = 34)


# Otros tipos de datos que podríamos pasar:

lista = ['JavaScript', 'Python', True, 65]
number = 33

def usar_tipos_de_datos(lista, number):
    print(lista)
    print(number)

usar_tipos_de_datos(lista, number)

# Recursión (recursividad) de una función [Se puede considerar en cierta forma un bucle]

# Ejemplo del factorial 
# 0! = 1
# n! = n * (n-1) para n > 0

def factorial(n):
    # Caso base 0! = 1
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = 3
print(f"El factorial de {numero} es {factorial(numero)}")