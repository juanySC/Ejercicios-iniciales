import matplotlib.pyplot as plt  # Importamos la libreria para crear graficos 2D
from itertools import combinations  # Para generar combinaciones de conjuntos
import matplotlib.patches as patches


MAX_CONJUNTOS = 10
MAX_ELEMENTOS = 15

def ingresar_conjuntos():
    conjuntos = []
    total = int(input(f"Cantidad de conjuntos a ingresar (max {MAX_CONJUNTOS}): "))
    if total < 1 or total > MAX_CONJUNTOS:
        print("Cantidad invalida.")
        return []
    
    #evalua si entra
    for i in range(total):
        #set() conjunto de elementos unicos desordenados
        conjunto = set()
        n = int(input(f"\nCantidad de elementos para el conjunto {i+1} (max {MAX_ELEMENTOS}): "))
        #evaluo cantidad de elementos
        if n < 1 or n > MAX_ELEMENTOS:
            print("Cantidad invalida.")
            return []
        print(f"Ingrese los elementos del conjunto {i+1}:")
        while len(conjunto) < n:
            elem = input(f"Elemento {len(conjunto)+1}: ").strip()
            if elem == "":
                print("Elemento vacio, ignorado.")
            elif elem in conjunto:
                print("Elemento duplicado, ignorado.")
            else:
                conjunto.add(elem)
        conjuntos.append(conjunto)
    return conjuntos

def mostrar_conjuntos(conjuntos):
    print("\nConjuntos ingresados:")
    for i, c in enumerate(conjuntos):
        print(f"Conjunto {i+1}: {{ {', '.join(sorted(c))} }}")

def union(a, b):
    return a.union(b)

def interseccion(a, b):
    return a.intersection(b)

def diferencia(a, b):
    return a.difference(b)

def diferencia_simetrica(a, b):
    return a.symmetric_difference(b)

def complemento(universal, a):
    return universal.difference(a)

def crear_universal(conjuntos):
    universal = set()
    for c in conjuntos:
        universal.update(c)
    return universal

def graficar_venn(conjunto_a, conjunto_b, resultado, operacion, nombre_a="A", nombre_b="B"):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Dibujar círculos
    circulo_a = patches.Circle((4, 3), 2, color='red', alpha=0.5, label=nombre_a)
    circulo_b = patches.Circle((6, 3), 2, color='blue', alpha=0.5, label=nombre_b)
    ax.add_patch(circulo_a)
    ax.add_patch(circulo_b)

    # Títulos de los conjuntos
    ax.text(3, 5, nombre_a, fontsize=12, ha='center')
    ax.text(7, 5, nombre_b, fontsize=12, ha='center')

    # Mostrar elementos según operación
    if operacion == "union":
        elementos = conjunto_a.union(conjunto_b)
    elif operacion == "interseccion":
        elementos = conjunto_a.intersection(conjunto_b)
    elif operacion == "diferencia":
        elementos = conjunto_a.difference(conjunto_b)
    elif operacion == "diferencia_simetrica":
        elementos = conjunto_a.symmetric_difference(conjunto_b)
    else:
        elementos = resultado  # Por si ya está calculado

    # Texto en el centro
    ax.text(5, 3, '\n'.join(sorted(elementos)), ha='center', va='center', fontsize=10)

    plt.title(f"Operación: {operacion}")
    plt.show()


def menu_operaciones(conjuntos):
    while True:
        print("\nOperaciones disponibles:")
        print("1. Union")
        print("2. Interseccion")
        print("3. Diferencia (A - B)")
        print("4. Diferencia simetrica")
        print("5. Complemento (respecto al universal)")
        print("0. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Entrada invalida.")
            continue

        if opcion == 0:
            print("Programa finalizado.")
            break
        elif opcion in [1, 2, 3, 4]:
            try:
                a = int(input("Ingrese el numero del primer conjunto: ")) - 1
                b = int(input("Ingrese el numero del segundo conjunto: ")) - 1
                if a not in range(len(conjuntos)) or b not in range(len(conjuntos)):
                    print("Numero de conjunto invalido.")
                    continue
                if opcion == 1:
                    resultado = union(conjuntos[a], conjuntos[b])
                    print("Union:", resultado)
                    graficar_venn(conjuntos[a], conjuntos[b], resultado, "union")
                elif opcion == 2:
                    resultado = interseccion(conjuntos[a], conjuntos[b])
                    print("Interseccion:", resultado)
                    graficar_venn( conjuntos[a], conjuntos[b],resultado, "Intersección")
                elif opcion == 3:
                    resultado = diferencia(conjuntos[a], conjuntos[b])
                    print("Diferencia:", resultado)
                    graficar_venn(conjuntos[a], conjuntos[b],resultado, "Diferencia")
                elif opcion == 4:
                    resultado = diferencia_simetrica(conjuntos[a], conjuntos[b])
                    print("Diferencia simetrica:", resultado)
                    graficar_venn(conjuntos[a],conjuntos[b],resultado, "Diferencia simetrica")
            except ValueError:
                print("Entrada invalida.")
        elif opcion == 5:
            try:
                a = int(input("Ingrese el numero del conjunto: ")) - 1
                if a not in range(len(conjuntos)):
                    print("Numero de conjunto invalido.")
                    continue
                universal = crear_universal(conjuntos)
                resultado = complemento(universal, conjuntos[a])
                print("Complemento:", resultado)
            except ValueError:
                print("Entrada invalida.")
        else:
            print("Opcion invalida.")

def main():
    conjuntos = ingresar_conjuntos()
    if conjuntos:
        mostrar_conjuntos(conjuntos)
        menu_operaciones(conjuntos)

if __name__ == "__main__":
    main()

