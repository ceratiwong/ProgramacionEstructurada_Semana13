lista = []

def divisiones_entre_dos(n):
    pasos = 0
    while n > 1:
        n = n // 2      # el problema se reduce a la mitad en cada vuelta
        pasos += 1
    return pasos

print(divisiones_entre_dos(1000))   # 9  → ¡solo 9 pasos para 1000!

def mostrar_parejas(lista):
    for a in lista:          # n vueltas
        for b in lista:      # n vueltas por cada vuelta externa
            print(a, b)      # se ejecuta n × n = n² veces

def agregar_elemento_lista():
    contador_elementos = 0
    while True:
        try:
            print(f"Elemento #{contador_elementos + 1}.")
            elemento = input("Ingrese un valor: ").strip()
            if not elemento:
                raise IndexError  # Dispara el error si el valor está vacío
            
            lista.append(elemento)
            contador_elementos += 1
            print(f"Elemento \"{elemento}\" agregado satisfactoriamente.")
            
            # Bucle con try...except para validar la respuesta (s/n)
            while True:
                try:
                    respuesta = input("¿Desea agregar otro elemento? (S/N): ").strip()
                    
                    if not respuesta:
                        raise IndexError  # Provoca IndexError si presionó Enter o solo espacios
                    
                    if respuesta == "S":
                        print()
                        break  # Regresa al bucle principal para agregar otro elemento
                    elif respuesta == "N":
                        print("Finalizando el programa...")
                        return lista  # Finaliza la función y retorna la lista
                    else:
                        print("Opción inválida. Debe ingresar \"S\" para sí o \"N\" para no.\n")
                        
                except IndexError:
                    print("Error. No ingresó ninguna respuesta. Intente nuevamente.\n")

        except IndexError:
            print("Error. Ingrese un valor válido. Intente nuevamente.\n")

agregar_elemento_lista()
mostrar_parejas(lista)