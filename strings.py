####### STRING (Cadena de texto)
texto = "Este es un curso de Python por Sergie Code"

# str (string): Texto o cadena de caracteres
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimples = '''Este es un texto'''

###### TYPE
print(type(comillasSimples))

###### Arrays de caracteres
caracter = texto[4] # Podemos seleccionar un caracter por índice
print(caracter)

# Len (Length) (Saber el largo)
amplitud = len(texto)
print(amplitud)

# In: para saber si está incluído algo en el texto
print("Python" in texto) # devuelve un True o False según corresponda

# Not in : con la palabra reservada not podemos negar y pedir un resultado negativo
print("JavaScript" not in texto) # devuelve un True o False según corresponda

# Slice (cortar) una parte del texto
print(texto[11:16]) # Se imprimirá el fragmento que vaya desde el índice 11 al 16 (no incluído)
print(texto[:5]) # Se imprimirá el fragmento que vaya desde el comienzo al índice 5 (no incluído)
print(texto[38:]) # Se imprimirá el fragmento que vaya desde el índice 38 hasta el final
print(texto[-4:]) # Se imprimirá el fragmento que vaya desde 4 índices antes del final hasta el final
print(texto[:-37]) # Se imprimirá el fragmento desde el comienzo hasta el final 37 caracteres antes del final

# Modificadores de texto (mayúsculas, minúsculas, etc)
texto_con_espacios = "          hola mundo       "
texto_con_comas = "No/ se/ olviden/ de/ suscribirse"

mayusculas = texto.upper() # Obtendré el texto en mayúsculas
minusculas = texto.lower() # Obtendré el texto en minúsculas
sin_espacios = texto_con_espacios.strip() # Eliminará los espacios del comienzo y el final
reemplazo = texto_con_espacios.replace("mundo", "universo") # Reeamplazará mundo por universo
separar_por_comas = texto_con_comas.split("/") # Separará el texto por comas y nos devolverá una lista

# Métodos más usados
texto_a_modificar = "este es UN texto A MODIFICAR"
capitalizado = texto_a_modificar.capitalize() # Sólo quedará la primera letra como mayúscula
estaComenzando = texto_a_modificar.startswith("este")
estaFinalizando = texto_a_modificar.endswith("MODIFICAR")
titulo = texto_a_modificar.title() # Pone en mayúscula cada palabra
contador = texto_a_modificar.count("e") # Cuantas veces aparece la e en el texto
encontrador = texto_a_modificar.find("texto") # Nos devuelve el índice donde comienza la palabra buscada

# Concatenar
a = "Hola"
b = "Mundo"
c = a + " " + b
print(c) # Imprimirá concatenado

# F-Strings (template strings)
num = 5
nombre = "Pedrito"
variable = "edad"
txt = f"La {variable} de {nombre} es de {num:.2f}" # Nos permite utilizar variables en texto y formatearlas

resultado = f"El resultado de 69 x 75 es {69*75}"

# Escapes \ (backslash - barra invertida)
escape = "Mi país favorito es \"Lituania\" por que me dio la ciudadanía europea"
directorio = "El directorio donde está almacenado mi mayor secreo es c:\\secreto\\archivo.txt"
salto_de_linea = "Quiero hacer un \nsalto de linea"

