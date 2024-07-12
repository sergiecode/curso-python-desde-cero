# LISTAS: colección (array) que permite almacenar múltiples elementos en una sola variable
# Características: ordenada (podemos ingresar a un elemento por índice) y es mutable

# indices:     0         1        2        3
frutas = ["Naranja", "Manzana", "Pera", "Pera"]  # Permite duplicados
longitud = len(frutas)  # saber la cantidad de elementos que

listaStrings = ["alfa", "beta", "gamma"]
listaNumbers = [0, 1, 2, 3, 4]
listaBooleans = [True, True, False]
listaMixta = ["alfa", 1, False]

tipo = type(listaBooleans) # Esto nos indicará  que tipo de datos es: "list"

listaDesdeConstructor = list(('Beta', 2, True)) # Hay que utilizar el constructor list y doble paréntesis

# Acceder a los datos:

naranja = frutas[0]
parteLista = frutas[1:3] # Desde el 1(manzana) hasta el 3 (no inclusive)
desdeComienzo = frutas[:-2] # Desde el comienzo hasta el dos no inclúido
hastaFinal = frutas[2:] # Desde el dos hasta el final

# Verificar si existe un elemento

if "Manzana" in frutas: # Utilizando la palabra "in" podemos saber si un elemento está presente
    print("Sí, está incluído")

# Como cambiar los datos de la lista
# indices:        0          1        2         3         4 
tecnologias = ['Python', 'Django', 'Flask', 'ReactPy', 'Pandas']

tecnologias[3] = 'TensoFlow' # Reemplazar el elemento de un índice particular
tecnologias[2:4] = ['NumPy', 'Scrapy'] # Reemplazar una parte de la lista

# Agregar elementos:
tecnologias.insert(2, 'Flask') # Insertar un nuevo elemento en un índice específico
tecnologias.append('TensorFlow') # Agregamos un elemento nuevo al final de la lista

frontend = ('Angular', 'React', 'Vue')
tecnologias.extend(frontend) # Agregar cualquier tipo de colección a un lista (fusión)

# Quitar elementos:
tecnologias.remove('Vue') # Se remueve el elemneto que coincida con lo que pasemos como argumetno
tecnologias.pop() # Podemos eliminar un elemento de un índice específico y si no especificamos se eliminará el último
del tecnologias[7] # Usando la palabra del podemos especificar el elemento a eliminar

listaABorrar = ['Python', 'Django', 'Flask', 'ReactPy', 'Pandas']
listaABorrar.clear() # Vaciaría la lista

# Recorrer listas 

for tecnologia in tecnologias:
    print(tecnologia)

for i in range(len(tecnologias)): # De esta forma podemos tener el índice del elemento iterable al recorrer la lista
    print(f"{i+1}. {tecnologias[i]}")

[print(tecnologia) for tecnologia in tecnologias] # Este sería el shorthand para una impresión de lista iterable

# Ejemplo práctico:

listaConY = []

for tecnologia in tecnologias:
    if "y" in tecnologia:
        listaConY.append(tecnologia)
#              lo que se agrega  |  el bucle                    | la condición
lista2conY = [tecnologia.upper() for tecnologia in tecnologias if "y" in tecnologia] # Shorthand del ejemplo de arriba

# Ordenar una lista:
tecnologias.sort() # En caso de no especificar ordenara alfabéticamente o de forma asc
numeros = [7,9,5,3,8,6,4,2]
numeros.sort(reverse=True) # En este caso ordenara de forma DESC
tecnologias.reverse() # Ordenar exactamente al revés tal cual estaba la lista

# Copiar una lista:

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
meses2 = ['Junio','Julio','Agosto','Septiembre']
copiaMeses = meses.copy()
copiaMeses2 = list(meses) # usando el costructor

joinMeses = meses + meses2 # Podemos juntar la listas (JOIN) utilizando el símbolo +
meses.extend(meses2) # Junta las dos listas en la lista mencionada
