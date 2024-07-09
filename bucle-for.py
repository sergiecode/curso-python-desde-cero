## BUCLES: estructura que se repite mientras la condición sea verdadera
## BUCLE FOR:

tecnologias = ['Python', 'JavaScript', 'Java', 'C#', 'Angular', 'React', 'NodeJS', 'Ruby', 'R', 'Django'] # esto es una lista
x = 1

# ¿Cómo iterar una estructura de datos (lista, tupla, etc)
for tecnologia in tecnologias:
    print(f"{x}. {tecnologia}")
    x += 1
else:
    print("Esas fueron todas las tecnologias que sabe Pedrito")

# ¿Cómo iterar un string (texto)?
for letra in "Python":
    print(letra)

# ¿Cómo iterar un rango de números? 
for x in range(5): # Range imprime desde cero al número que colocamos sin incluirlo
    print(x)

for x in range(2,7): # Range imprime desde el primer número al segundo número sin incluirlo
    print(x)

for x in range (2,11,2): # El tercer parámetro nos sirve para poner intervalos
    print(x)

letras = ['a','b','c']
numeros = [1,2,3]

for l in letras:
    for n in numeros:
        print(l,n)

# a1, a2, a3, b1, b2, b3, c1, c2, c3