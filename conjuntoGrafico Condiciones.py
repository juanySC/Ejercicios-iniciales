﻿import pygame
import sys

# Bucle para verificar entrada válida
while True:
     #atrapa errores
    try:
        entradaConjunto = int(input("¿Cuántos conjuntos desea crear? (máximo 10): "))

        #si esta en el rango entra
        if 1 <= entradaConjunto <= 10:
            #crea una biblioteca vacia
            conjuntos = {}

             #recorre los conjuntos que ingreso el usuario
            for i in range(entradaConjunto):
                nombre = input(f"\nIngrese el nombre del conjunto ej(A,B) #{i+1}: ")
                 #llamo al 'nombre' para que sea mas facil de visualizar
                 
                 #si esta en el rango entra
                
                entradaElementos = input(f"Ingrese los elementos del conjunto '{nombre}', separados por comas (,) (max 15): ")
                #set es un conjunto de elementos unicos y no ordenados
                elementos = set(x.strip() for x in entradaElementos.split(','))
               
                conjunto = set(elementos)
                conjuntos[nombre] = conjunto
           

            #imprime en pantalla los elementos ingresados
            print("\nConjuntos ingresados:")
            #lo que creo el usuario y lo que se almacena en el diccionario
            for nombre, conjunto in conjuntos.items():
                print(f"{nombre}: {conjunto}")

             #ahora seleccionar los conjutos a visualiza
            print("\nSeleccione dos conjuntos para el diagrama de Venn:")
            for nombre in conjuntos:
                print(f"- {nombre}")

            #strip() ayuda a eliminar espacios en blanco
            conjunto1 = input("\nIngrese el primer nombre: ").strip()
            conjunto2 = input("\nIngrese el segundo nombre: ").strip()
            conjunto3 = input("\nIngrese el segundo nombre: ").strip()

            #Comparo si estos estan en la lista que dio anteriormente
            #el usuario
            if conjunto1 not in conjuntos or conjunto2 not in conjuntos or conjunto3 not in conjuntos:
                print("Uno o ambos nombres no están en la lista.")
                sys.exit()

            
            conjunto_a = conjuntos[conjunto1]
            conjunto_b = conjuntos[conjunto2]
            conjunto_c = conjuntos[conjunto3]

            #condiciones de conjuntos
            print("Opcion de operaciones en conjuntos para graficarlo")
            print("1. Union")
            print("2. Intersección")
            print("3. Complemento")
            print("4. Diferencia")
            print("5. Diferencia simétrica")

            opcion = input("Ingrese la opción que desee: ")

            if opcion == "1":
                resultado = conjunto_a | conjunto_b | conjunto_c
                print("\n union")
                print(resultado)
                titulo = f"{conjunto1} ∩ {conjunto2}"
                print()
            elif opcion == "2":
                resultado = conjunto_a & conjunto_b & conjunto_c
                print("\n intersección")
                print(resultado)
                titulo = f"{conjunto1} u {conjunto2}"
            elif opcion == "3":
                print("Aun no se")
            elif opcion == "4":
                resultado = conjunto_a - conjunto_b
                titulo = f"{conjunto1} - {conjunto2}"
                print("\n diferencia")
                print(resultado)
            elif opcion == "5":
                resultado = conjunto_a ^ conjunto_b
                titulo = f"{conjunto1} df {conjunto2}"
                print("\n diferencia simetrica")
                print(resultado)
            else: 
                print("Opción no disponible")

            #visualizar de manera grafica
            pygame.init()
            ancho, alto = 600, 400
            pantalla = pygame.display.set_mode((ancho, alto))
             #que es lo que se mostrara en pantalla
            pygame.display.set_caption(f"Diagrama de Venn: {conjunto1} ∩ {conjunto2}")
            fuente = pygame.font.SysFont(None, 24)

            # Colores
            ROJO = (255, 0, 0, 120)
            AZUL = (0, 0, 255, 120)
            VERDE = (0,255,0,120)
            BLANCO = (255, 255, 255)
            NEGRO = (0, 0, 0)

            # Superficies con transparencia
            circuloRojo = pygame.Surface((300, 300), pygame.SRCALPHA)
            circuloAzul = pygame.Surface((300, 300), pygame.SRCALPHA)
            circuloVerde = pygame.Surface((300,300), pygame.SRCALPHA)
            #dibujo los conjuntos
            pygame.draw.circle(circuloRojo, ROJO, (150, 150), 100)
            pygame.draw.circle(circuloAzul, AZUL, (150, 150), 100)
            pygame.draw.circle(circuloVerde, VERDE, (150,150),100)

            # Función para escribir texto en pantalla
            def escribirElementos(elementos, posInicial):
                x, y = posInicial
                for element in elementos:
                    texto = fuente.render(str(element), True, NEGRO)
                    pantalla.blit(texto, (x, y))
                    y += 20

              # Repeticion del dibujo y se cierra cuando termina
            ejecutando = True
            while ejecutando:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        ejecutando = False

                 #mantiene la ventana abierta
                pantalla.fill(BLANCO)

                # Dibuja los círculos
                pantalla.blit(circuloRojo, (150, 100))
                pantalla.blit(circuloAzul, (250, 100))
                pantalla.blit(circuloVerde,(200, 80))

                # Dibuja las etiquetas
                etiqueta1 = fuente.render(conjunto1, True, NEGRO)
                etiqueta2 = fuente.render(conjunto2, True, NEGRO)
                pantalla.blit(etiqueta1, (170, 90))
                pantalla.blit(etiqueta2, (370, 90))

                # Dibuja los elementos
                    # Mostrar elementos según la operación
                if opcion == "1":  # Union
                    titulo = f"{conjunto1} ∪ {conjunto2}"
                    escribirElementos(resultado, (260, 150))
                  
                elif opcion == "2":  # Interceccion
                    escribirElementos(conjunto_a - resultado, (160, 120))
                    escribirElementos(conjunto_b - resultado, (360, 120))
                    escribirElementos(resultado, (260, 150))
                elif opcion == "3":
                    escribirElementos()
                elif opcion == "4":  # Diferencia A - B
                    escribirElementos(resultado, (160, 120))
                elif opcion == "5":  # Diferencia simétrica
                    escribirElementos(resultado, (260, 150))

                pygame.display.flip()  # Actualizar pantalla

            pygame.quit()
            sys.exit()

        else:
            print("\nIngrese un número entre 1 y 10.")

    except ValueError:
        print("\nLa entrada no es válida")
        print("Intente ingresar un numero entero")
