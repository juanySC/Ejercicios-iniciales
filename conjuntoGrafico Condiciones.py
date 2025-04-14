import pygame
import sys

# Bucle para verificar entrada válida
while True:
    #atrapa errores
    try:
        entradaConjunto = int(input("¿Cuántos conjuntos desea crear? (máximo 10): "))
        
        #si esta en el rango entra
        if 1 <= entradaConjunto <= 10:
            #crea un diccionario vacio
            conjuntos = {}  

            #recorre los conjuntos que ingreso el usuario
            for i in range(entradaConjunto):
                nombre = input(f"\nIngrese el nombre del conjunto #{i+1}: ")
                #llamo al 'nombre' para que sea mas facil de visualizar
                entradaElementos = input(f"Ingrese los elementos del conjunto '{nombre}', separados por comas (,): ")
                #set es un conjunto de elementos unicos y no ordenados
                conjunto = set(entradaElementos.split(','))
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

            #Comparo si estos estan en la lista que dio anteriormente
            #el usuario
            if conjunto1 not in conjuntos or conjunto2 not in conjuntos:
                print("Uno o ambos nombres no están en la lista.")



            break  # Sale del bucle al temrminar la tarea

        else:
            print("\nIngrese un número entre 1 y 10.")

    except ValueError:
        print("\nLa entrada no es válida")
        print("Intente ingresar un numero entero")
