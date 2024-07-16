# DICCIONARIO: colección (array) que permite almacenar múltiples elementos en una sola variable
# Características: Colección de pares clave-valor(key-value) desordenada y mutable

diccionario = {
    "nombre": "Sergie Code",
    "youtube": "www.youtube.com/@sergiecode",
    "tecnologias": ["Python", "Javascript"],
    "edad": 34,
    "direccion": {"calle": "Av Argentina", "numero": 123, "ciudad": "Londres"},
}

tipo = type(diccionario) # Nos indica el tipo de dato <class 'dict'>
longintud = len(diccionario) # Nos indica la cantidad de claves-valor que tiene el diccionario
contructorDiccionario = dict(nombre = "Sergie Code", youtube = "www.youtube.com/@sergiecode") # Se puede crear con constructor

# ¿Cómo accedo a cada propiedad?

nombre = diccionario["nombre"]
youtube = diccionario.get("youtube")
keys = diccionario.keys() # el tipo de dato que devuelve se llama <class 'dict_keys'>
values = diccionario.values() # el tipo de dato que devuelve se llama <class 'dict_values'>

items = diccionario.items() # nos devuelve tuplas de clave-valor en una lista // <class 'dict_items'>

# if "tecnologias" in diccionario: # Con esto podemos comprobar si una key existe pero no un valor
#     print("Sí, existe esta key")

# CAMBIO de valores en un diccionario

diccionario["tecnologias"] = ['Python', 'JavaScript', 'Java', 'Node']
diccionario.update({"direccion": {"calle": "Liverpool Street", "numero": 123, "ciudad": "Londres"},})

# AGREGAR ITEMS:

diccionario["profesion"] = "Programador"
diccionario.update({ 'Comida Favorita': ' Milanesa'})

# ELIMINAR ITEMS:

diccionario.pop("Comida Favorita") # Eliminar un elemento puntual
diccionario.popitem() # Eliminaría última característica agregada
del diccionario["edad"]
diccionario.clear() # esto deja vacío el diccionario

# BUCLES (LOOPS ) para diccionarios:

curso_python = {
    "nombre": "Python desde Cero",
    "duracion": 6,
    "dificultad": "media",
}

# for key in curso_python: # el bucle for común hará un recorrido de las keys
#     print(f"{key.capitalize()}: {curso_python[key]}")

# for values in curso_python.values(): # este bucle recorrerá solo los valores
#     print(values)

# for key, value in curso_python.items(): #desempaqueto la tupla de cada uno de los elementos de la lista que devuelve items
#     print(key, value)

# COPIAS de diccionarios:

copia = curso_python.copy() #copia exacta pero apuntando a otra dirección de memoria
copia2 = dict(curso_python) #copia usando constructor

# DICCIONARIOS ANIDADOS:

hijo1 = {
    "nombre" : "Pedro",
    "edad" : 5
}
hijo2 = {
    "nombre" : "Alan",
    "edad" : 7
}
hijo3 = {
    "nombre" : "Enzo",
    "edad" : 9
}

familia = {
    "hijo1": hijo1,
    "hijo2": hijo2,
    "hijo3": hijo3,
}

nombreHijo1 = familia["hijo1"]["nombre"]

for x,obj in familia.items():
    print(x)
    for y in obj:
        print(f"{y.capitalize()}: {obj[y]}")