# SETS: colección (array) que permite almacenar múltiples elementos en una sola variable
# Características: coleccion desordenada de elementos únicos (no ordenados)
# * Se pueden agregar y eliminar elementos pero los elemetos nos son "cambiables" ya que no tienen un orden

conjunto = {1, 1, 2, 2, 3}  # los elementos que estén duplicados serán omitidos

longitud = len(conjunto)  # la longitud o cantidad de elmentos del conjunto (no tomará en cuenta los duplicados)
tipo = type(conjunto)  # para saber el tipo <class 'set'>
conjuntoConstructor = set(("Este", "es", "un", "conjunto")) # creamos un conjunto usando el contructor

# if "conjunto" in conjuntoConstructor: # podemos usar IN para saber si un elemento está presente
#     print("Sí está la palabra")

# if "Python" not in conjuntoConstructor: # not in para saber si un elemento no está presente
#     print("Python no se encuentra en el conjunto")

# Agregar elementos a un conjunto (SET)

telefonos = {'Xiaomi', 'Samsung', 'Motorola'}
telefonos2 = ['Huawei', 'OnePlus', 'Nokia', 'Xiaomi' ] #puede ser cualquier colección

telefonos.add("Iphone") # Agregar un elemento

telefonos.update(telefonos2) # Con update sumamos otra colección(puede ser cualquier colección) a nuestro conjunto

# Eliminar elementos (al no tener órden especifico hay que tener mucho cuidado en el borrado)

autos = { 'Ford', 'Peugeot', 'Fiat', 'Renault', 'Ferrari' }

autos.remove('Ferrari') # Se borra un elemento que coincida exactamente con lo pasado por argumento (Da un error si no existe)
autos.discard('Fiat') # Se borra un elemento que coincida exactamente con lo pasado por argumento (no da un error si no existe)

autos.pop() # Eliminará uno de forma aleatoria

autos.clear() # borrar todos los elementos presentes en el conjunto

# Recorrer los elementos con bucles

# tecnologias = { 'Python', 'C#', 'Java', 'Node'}

# for tecnologia in tecnologias:
#     print(tecnologia)

# [print(tecnologia) for tecnologia in tecnologias] # Este sería el shorthand para una impresión de conjunto iterable


# Join de conjuntos (Teoría de conjuntos de la matemática)

a = {1,2,3,4,5}
b = {1,3,5,7,9}

booleanos = {True, False}

# Union: devuelve todos los elementos de ambos conjuntos  (a diferencia del update no modifica el conjunto original)
u = a.union(b) # acepta varias colecciones (pueden ser listas o tuplas)
u2 = a | b # es exactamente lo mismo que usar union

# a.update(b) # update modifica el conjunto original

# Intersección: va a devolver los elementos que tengan en común ambos conjuntos
i = a.intersection(b)
i2 = a & b # esto es exactamente lo mismo que usar intersection

# a.intersection_update(b) # Intersection update modifica el conjunto original

# Comportamiento con booleanos:
booleanos_union = a.union(booleanos) # True y 1 se consideran el mismo valor por lo cual solo se agregará False
booleanos_intersection = a.intersection(booleanos) # La única intersección es True ya que se considera igual a 1

# Diferencias: devolver los elementos del primer conjunto que no estén presentes en el otro conjunto

d1 = a.difference(b)
d2 = a - b # es exactamente lo mismo que usar difference

# a.difference_update(b) # Difference update modifica el conjunto original

# Diferencia simétrica: developer los elementos que no estén presentes en ambos conjuntos

ds1 = a.symmetric_difference(b)
ds2 = a ^ b # es exactamente igual que usar symmetric_difference

# a.symmetric_difference_update(b) # symmetric difference update modifica el conjunto original

