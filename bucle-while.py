## BUCLES: estructura que se repite mientras la condición sea verdadera
## BUCLE WHILE: 

x = 1

while x <= 10:
    print(f"Hola a todos estoy dentro de un bucle y x vale {x}")
    x += 1

    if x == 5:
        break # Esto hace que salga del bucle

    if x == 15:
        continue # saltea las líneas de acá en adelante

else:
    print(f"Ya no se cumplió la condición del bucle porque x es {x}")



## EJEMPLO PRACTICO

while True:
    print("No te olvides de suscribirte a mi canal @sergiecode")
    respuesta = input("¿Desea salir? (s/n)").strip().lower()
    if respuesta == 's':
        break