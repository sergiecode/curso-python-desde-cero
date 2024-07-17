# Funciones Lambda: son funciones anónimas y cortas (de una sola línea de código)

# SINTAXIS:
# lambda arg1, arg2, etc : retorno

def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a // b



# Ejemplos (aunque no deberíamos asignar a una variable una lambda como buena práctica)
suma_lambda = lambda a,b : a + b 
resta_lambda = lambda a,b : a - b 
multiplicacion_lambda = lambda a,b : a * b 
division_lambda = lambda a,b : a // b 


# Ejemplo más realista [ Constructor de funciones ]

def creador_funciones_multiplicacion(n):
    return lambda a : a * n

duplicador = creador_funciones_multiplicacion(2)
triplicador = creador_funciones_multiplicacion(3)
cuadriplicador = creador_funciones_multiplicacion(4)

print(duplicador(5))
print(triplicador(5))
print(cuadriplicador(5))

# Ejemplo práctico de lambda en filter

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 == 0,  numeros))
print(pares)